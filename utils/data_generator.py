"""Generate sample demo data for FieldOps AI"""
from faker import Faker
from random import choice, randint, uniform, sample
from datetime import datetime, timedelta
import random

from database.session import SessionLocal
from database.models import *

fake = Faker()

# Sample company: Toronto HVAC Solutions
COMPANY_NAME = "Toronto HVAC Solutions"
TORONTO_LAT = 43.6532
TORONTO_LNG = -79.3832

# Job types and specialties
JOB_TYPES = ["HVAC Repair", "AC Installation", "Furnace Maintenance", "Electrical Wiring", 
             "Duct Cleaning", "Heat Pump Service", "Emergency Repair", "Preventive Maintenance"]

TECHNICIAN_SPECIALTIES = ["HVAC", "Electrical", "Plumbing", "General Repair"]

INVENTORY_CATEGORIES = {
    "HVAC Parts": ["Air Filter", "Thermostat", "Refrigerant", "Compressor", "Fan Motor"],
    "Electrical": ["Wire (14 AWG)", "Circuit Breaker", "Outlet", "Switch", "Electrical Tape"],
    "Tools": ["Multimeter", "Screwdriver Set", "Pipe Wrench", "Drill Bits"],
    "Supplies": ["Duct Tape", "Insulation", "Solder", "Copper Pipe"]
}

def generate_customers(count=30):
    """Generate sample customers"""
    db = SessionLocal()
    try:
        existing = db.query(Customer).count()
        if existing > 0:
            return  # Already has data
        
        customers = []
        for _ in range(count):
            customer = Customer(
                name=fake.company(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.street_address(),
                city="Toronto",
                province="ON",
                postal_code=fake.postalcode()
            )
            customers.append(customer)
        
        db.add_all(customers)
        db.commit()
        print(f"Generated {count} customers")
    finally:
        db.close()

def generate_technicians(count=12):
    """Generate sample technicians"""
    db = SessionLocal()
    try:
        existing = db.query(Technician).count()
        if existing > 0:
            return
        
        technicians = []
        for i in range(count):
            # Vary home base locations around Toronto
            lat_offset = uniform(-0.3, 0.3)
            lng_offset = uniform(-0.3, 0.3)
            
            technician = Technician(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                specialty=choice(TECHNICIAN_SPECIALTIES),
                hourly_rate=uniform(65.0, 95.0),
                home_base_lat=TORONTO_LAT + lat_offset,
                home_base_lng=TORONTO_LNG + lng_offset,
                rating=uniform(4.2, 5.0),
                is_active=True
            )
            technicians.append(technician)
        
        db.add_all(technicians)
        db.commit()
        print(f"Generated {count} technicians")
    finally:
        db.close()

def generate_inventory():
    """Generate inventory items"""
    db = SessionLocal()
    try:
        existing = db.query(InventoryItem).count()
        if existing > 0:
            return
        
        items = []
        sku_counter = 1000
        
        for category, parts in INVENTORY_CATEGORIES.items():
            for part_name in parts:
                item = InventoryItem(
                    name=part_name,
                    sku=f"SKU-{sku_counter:06d}",
                    category=category,
                    quantity=randint(5, 100),
                    unit_price=uniform(10.0, 500.0),
                    reorder_level=randint(5, 25),
                    supplier=fake.company()
                )
                items.append(item)
                sku_counter += 1
        
        db.add_all(items)
        db.commit()
        print(f"Generated {len(items)} inventory items")
    finally:
        db.close()

def generate_work_orders(count=50):
    """Generate sample work orders"""
    db = SessionLocal()
    try:
        existing = db.query(WorkOrder).count()
        if existing > 0:
            return
        
        customers = db.query(Customer).all()
        technicians = db.query(Technician).all()
        
        if not customers or not technicians:
            return
        
        work_orders = []
        base_date = datetime.now() - timedelta(days=30)
        
        for i in range(count):
            customer = choice(customers)
            technician = choice(technicians) if random.random() < 0.7 else None
            job_type = choice(JOB_TYPES)
            
            # Random date in past 30 days or future 7 days
            days_offset = randint(-30, 7)
            scheduled_date = base_date + timedelta(days=days_offset)
            
            # Job location around Toronto
            lat = TORONTO_LAT + uniform(-0.2, 0.2)
            lng = TORONTO_LNG + uniform(-0.2, 0.2)
            
            status = choice(["pending", "scheduled", "in_progress", "completed"])
            
            # Estimate duration and cost
            estimated_duration = uniform(2.0, 8.0)
            hourly_rate = technician.hourly_rate if technician else 75.0
            estimated_cost = estimated_duration * hourly_rate * uniform(1.2, 1.8)
            
            work_order = WorkOrder(
                customer_id=customer.id,
                assigned_technician_id=technician.id if technician else None,
                job_type=job_type,
                description=f"{job_type} service for {customer.name}",
                location=f"{fake.street_address()}, Toronto, ON",
                lat=lat,
                lng=lng,
                status=status,
                priority=choice(["low", "medium", "high", "urgent"]),
                scheduled_date=scheduled_date if status in ["scheduled", "in_progress", "completed"] else None,
                estimated_duration=estimated_duration,
                estimated_cost=estimated_cost
            )
            
            # Add actuals if completed
            if status == "completed":
                work_order.actual_duration = estimated_duration * uniform(0.8, 1.2)
                work_order.actual_cost = work_order.estimated_cost * uniform(0.9, 1.1)
                work_order.actual_start_time = scheduled_date.replace(hour=randint(8, 10))
                work_order.actual_end_time = work_order.actual_start_time + timedelta(
                    hours=work_order.actual_duration
                )
            
            work_orders.append(work_order)
        
        db.add_all(work_orders)
        db.commit()
        print(f"Generated {count} work orders")
        
        # Generate parts usage for completed jobs
        generate_job_parts()
        
        # Generate timesheets
        generate_timesheets()
        
        # Generate invoices for completed jobs
        generate_invoices()
        
    finally:
        db.close()

def generate_job_parts():
    """Generate parts usage for completed jobs"""
    db = SessionLocal()
    try:
        completed_jobs = db.query(WorkOrder).filter(
            WorkOrder.status == "completed"
        ).all()
        
        inventory_items = db.query(InventoryItem).all()
        
        if not completed_jobs or not inventory_items:
            return
        
        job_parts = []
        
        for job in completed_jobs[:len(completed_jobs)//2]:  # Add parts to ~50% of jobs
            num_parts = randint(1, 4)
            selected_parts = sample(inventory_items, min(num_parts, len(inventory_items)))
            
            for inv_item in selected_parts:
                quantity = randint(1, 5)
                job_part = JobPart(
                    work_order_id=job.id,
                    inventory_item_id=inv_item.id,
                    quantity_used=quantity,
                    unit_cost=inv_item.unit_price,
                    total_cost=inv_item.unit_price * quantity
                )
                job_parts.append(job_part)
        
        db.add_all(job_parts)
        db.commit()
        print(f"Generated {len(job_parts)} job parts entries")
    finally:
        db.close()

def generate_timesheets():
    """Generate timesheet entries"""
    db = SessionLocal()
    try:
        completed_jobs = db.query(WorkOrder).filter(
            WorkOrder.status == "completed",
            WorkOrder.assigned_technician_id.isnot(None)
        ).all()
        
        if not completed_jobs:
            return
        
        timesheets = []
        
        for job in completed_jobs:
            if job.actual_start_time and job.actual_end_time:
                check_in_lat = job.lat + uniform(-0.01, 0.01)
                check_in_lng = job.lng + uniform(-0.01, 0.01)
                
                check_out_lat = job.lat + uniform(-0.01, 0.01)
                check_out_lng = job.lng + uniform(-0.01, 0.01)
                
                hours_worked = job.actual_duration
                
                timesheet = Timesheet(
                    technician_id=job.assigned_technician_id,
                    work_order_id=job.id,
                    check_in_time=job.actual_start_time,
                    check_in_lat=check_in_lat,
                    check_in_lng=check_in_lng,
                    check_out_time=job.actual_end_time,
                    check_out_lat=check_out_lat,
                    check_out_lng=check_out_lng,
                    hours_worked=hours_worked,
                    is_verified=True,
                    has_anomaly=random.random() < 0.1  # 10% have anomalies
                )
                timesheets.append(timesheet)
        
        db.add_all(timesheets)
        db.commit()
        print(f"Generated {len(timesheets)} timesheets")
    finally:
        db.close()

def generate_invoices():
    """Generate invoices for completed jobs"""
    db = SessionLocal()
    try:
        completed_jobs = db.query(WorkOrder).filter(
            WorkOrder.status == "completed"
        ).all()
        
        if not completed_jobs:
            return
        
        invoices = []
        invoice_counter = 1000
        
        for job in completed_jobs[:len(completed_jobs)//2]:  # Invoice ~50% of jobs
            # Calculate costs
            labor_hours = job.actual_duration or job.estimated_duration
            technician = job.technician
            labor_rate = technician.hourly_rate if technician else 75.0
            labor_cost = labor_hours * labor_rate
            
            # Get parts cost
            parts = db.query(JobPart).filter(JobPart.work_order_id == job.id).all()
            materials_cost = sum([p.total_cost for p in parts])
            
            subtotal = labor_cost + materials_cost
            tax_amount = subtotal * 0.13  # 13% HST
            total_amount = subtotal + tax_amount
            
            # Random payment status
            is_paid = random.random() < 0.6  # 60% paid
            status = "paid" if is_paid else "pending"
            paid_date = job.scheduled_date + timedelta(days=randint(1, 30)) if is_paid else None
            
            invoice = Invoice(
                customer_id=job.customer_id,
                work_order_id=job.id,
                invoice_number=f"INV-{invoice_counter:05d}",
                invoice_date=job.scheduled_date + timedelta(days=1),
                due_date=job.scheduled_date + timedelta(days=30),
                labor_hours=labor_hours,
                labor_rate=labor_rate,
                labor_cost=labor_cost,
                materials_cost=materials_cost,
                subtotal=subtotal,
                tax_amount=tax_amount,
                total_amount=total_amount,
                status=status,
                paid_date=paid_date
            )
            
            invoices.append(invoice)
            invoice_counter += 1
        
        db.add_all(invoices)
        db.commit()
        print(f"Generated {len(invoices)} invoices")
    finally:
        db.close()

def load_demo_data():
    """Load all demo data"""
    print("Loading demo data for Toronto HVAC Solutions...")
    generate_customers(30)
    generate_technicians(12)
    generate_inventory()
    generate_work_orders(50)
    print("Demo data loaded successfully!")

if __name__ == "__main__":
    from database.session import init_db
    init_db()
    load_demo_data()

