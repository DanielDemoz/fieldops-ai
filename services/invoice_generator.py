"""Auto-invoice generator with PDF export"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime
from pathlib import Path
import os

from database.session import SessionLocal
from database.models import Invoice, WorkOrder, Customer

class InvoiceGenerator:
    """Generate PDF invoices"""
    
    def __init__(self):
        self.output_dir = Path("invoices")
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_pdf(self, invoice_id: int) -> str:
        """Generate PDF invoice"""
        db = SessionLocal()
        try:
            invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
            if not invoice:
                return None
            
            customer = invoice.customer
            work_order = invoice.work_order
            
            # Generate filename
            filename = f"invoice_{invoice.invoice_number}.pdf"
            filepath = self.output_dir / filename
            
            # Create PDF
            c = canvas.Canvas(str(filepath), pagesize=letter)
            width, height = letter
            
            # Header
            c.setFont("Helvetica-Bold", 20)
            c.drawString(1*inch, height - 1*inch, "INVOICE")
            
            # Company info
            c.setFont("Helvetica", 10)
            c.drawString(1*inch, height - 1.3*inch, "Toronto HVAC Solutions")
            c.drawString(1*inch, height - 1.45*inch, "123 Service Road")
            c.drawString(1*inch, height - 1.6*inch, "Toronto, ON M1A 1A1")
            c.drawString(1*inch, height - 1.75*inch, "Phone: (416) 555-0123")
            
            # Invoice details
            x_right = width - 1*inch
            y_top = height - 1*inch
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(x_right - 100, y_top, f"Invoice #{invoice.invoice_number}")
            
            c.setFont("Helvetica", 10)
            y = y_top - 20
            c.drawString(x_right - 100, y, f"Date: {invoice.invoice_date.strftime('%Y-%m-%d') if invoice.invoice_date else 'N/A'}")
            y -= 15
            c.drawString(x_right - 100, y, f"Due Date: {invoice.due_date.strftime('%Y-%m-%d') if invoice.due_date else 'N/A'}")
            y -= 15
            c.drawString(x_right - 100, y, f"Status: {invoice.status.upper()}")
            
            # Bill To
            y = height - 2.5*inch
            c.setFont("Helvetica-Bold", 12)
            c.drawString(1*inch, y, "Bill To:")
            y -= 20
            c.setFont("Helvetica", 10)
            c.drawString(1*inch, y, customer.name if customer else "N/A")
            y -= 15
            if customer:
                if customer.address:
                    c.drawString(1*inch, y, customer.address)
                    y -= 15
                if customer.city:
                    city_line = f"{customer.city}, {customer.province or ''} {customer.postal_code or ''}".strip()
                    c.drawString(1*inch, y, city_line)
            
            # Items table
            y = height - 4*inch
            
            # Table header
            c.setFont("Helvetica-Bold", 10)
            c.drawString(1*inch, y, "Description")
            c.drawString(4*inch, y, "Quantity")
            c.drawString(5*inch, y, "Rate")
            c.drawString(6.5*inch, y, "Amount")
            
            y -= 20
            c.setFont("Helvetica", 10)
            c.line(1*inch, y, 7.5*inch, y)
            y -= 20
            
            # Labor
            c.drawString(1*inch, y, "Labor")
            c.drawString(4*inch, y, f"{invoice.labor_hours:.2f} hrs")
            c.drawString(5*inch, y, f"${invoice.labor_rate:.2f}")
            c.drawString(6.5*inch, y, f"${invoice.labor_cost:.2f}")
            y -= 20
            
            # Materials
            if invoice.materials_cost > 0:
                c.drawString(1*inch, y, "Materials")
                c.drawString(4*inch, y, "-")
                c.drawString(5*inch, y, "-")
                c.drawString(6.5*inch, y, f"${invoice.materials_cost:.2f}")
                y -= 20
            
            # Other charges
            if invoice.other_charges > 0:
                c.drawString(1*inch, y, "Other Charges")
                c.drawString(4*inch, y, "-")
                c.drawString(5*inch, y, "-")
                c.drawString(6.5*inch, y, f"${invoice.other_charges:.2f}")
                y -= 20
            
            # Totals
            y -= 10
            c.line(1*inch, y, 7.5*inch, y)
            y -= 20
            
            c.drawString(6*inch, y, "Subtotal:")
            c.drawString(6.5*inch, y, f"${invoice.subtotal:.2f}")
            y -= 20
            
            c.drawString(6*inch, y, f"Tax ({invoice.tax_rate*100:.0f}%):")
            c.drawString(6.5*inch, y, f"${invoice.tax_amount:.2f}")
            y -= 20
            
            c.setFont("Helvetica-Bold", 12)
            c.drawString(6*inch, y, "Total:")
            c.drawString(6.5*inch, y, f"${invoice.total_amount:.2f}")
            
            # Footer
            y = 1*inch
            c.setFont("Helvetica", 8)
            c.drawString(1*inch, y, "Thank you for your business!")
            
            c.save()
            
            # Update invoice with PDF path
            invoice.pdf_path = str(filepath)
            db.commit()
            
            return str(filepath)
            
        except Exception as e:
            db.rollback()
            print(f"Error generating invoice: {e}")
            return None
        finally:
            db.close()

