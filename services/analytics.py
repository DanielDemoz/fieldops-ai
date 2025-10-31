"""Analytics and forecasting service"""
from datetime import datetime, timedelta
from typing import Dict, List
from collections import defaultdict

from database.session import SessionLocal
from database.models import WorkOrder, Invoice, Timesheet, JobPart

class AnalyticsService:
    """Analytics and KPI calculations"""
    
    def __init__(self):
        self.db = SessionLocal()
    
    def calculate_kpis(self) -> Dict:
        """Calculate key performance indicators"""
        try:
            kpis = {}
            
            # Average travel time (mock calculation)
            timesheets = self.db.query(Timesheet).filter(
                Timesheet.is_verified == True
            ).all()
            
            if timesheets:
                avg_travel = 25.0  # Mock: 25 minutes average
                kpis['avg_travel_time'] = avg_travel
            
            # Jobs per day (last 30 days)
            thirty_days_ago = datetime.now() - timedelta(days=30)
            completed_jobs = self.db.query(WorkOrder).filter(
                WorkOrder.status == "completed",
                WorkOrder.scheduled_date >= thirty_days_ago
            ).count()
            
            kpis['jobs_per_day'] = completed_jobs / 30.0
            
            # Profit per job
            invoices = self.db.query(Invoice).filter(
                Invoice.status == "paid"
            ).all()
            
            if invoices:
                total_revenue = sum([inv.total_amount for inv in invoices])
                total_cost = sum([inv.labor_cost + inv.materials_cost for inv in invoices])
                profit = total_revenue - total_cost
                kpis['profit_per_job'] = profit / len(invoices) if invoices else 0
            else:
                kpis['profit_per_job'] = 0
            
            # Material cost variance (mock)
            kpis['material_variance'] = 5.2  # 5.2% variance
            
            # Technician utilization (mock)
            kpis['utilization'] = 78.5  # 78.5% utilization
            
            # 30-day cash balance (from forecast)
            forecast = self.generate_cash_flow_forecast(30)
            if forecast:
                last_balance = forecast[-1]['predicted_balance']
                kpis['cash_balance_30d'] = last_balance
            else:
                kpis['cash_balance_30d'] = 0
            
            return kpis
            
        finally:
            self.db.close()
    
    def generate_cash_flow_forecast(self, days: int = 30) -> List[Dict]:
        """Generate cash flow forecast using simple projection"""
        try:
            # Get historical data
            invoices = self.db.query(Invoice).all()
            
            # Calculate average daily revenue and expenses
            paid_invoices = [inv for inv in invoices if inv.status == "paid"]
            total_revenue = sum([inv.total_amount for inv in paid_invoices])
            
            # Simple forecast: assume current trend continues
            daily_revenue = total_revenue / 30.0 if len(paid_invoices) > 0 else 500.0
            daily_expenses = daily_revenue * 0.6  # Assume 60% expenses
            
            # Current balance (mock)
            current_balance = 15000.0
            
            forecast = []
            for i in range(days):
                date = datetime.now() + timedelta(days=i)
                current_balance = current_balance + daily_revenue - daily_expenses
                
                # Add some variance
                variance = (i % 7) * 50  # Weekly pattern
                current_balance += variance
                
                forecast.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "predicted_balance": round(current_balance, 2)
                })
            
            return forecast
            
        finally:
            self.db.close()
    
    def get_job_completion_trends(self) -> List[Dict]:
        """Get job completion trends for last 30 days"""
        try:
            thirty_days_ago = datetime.now() - timedelta(days=30)
            completed_jobs = self.db.query(WorkOrder).filter(
                WorkOrder.status == "completed",
                WorkOrder.scheduled_date >= thirty_days_ago
            ).all()
            
            # Group by date
            daily_counts = defaultdict(int)
            for job in completed_jobs:
                if job.scheduled_date:
                    date_key = job.scheduled_date.strftime("%Y-%m-%d")
                    daily_counts[date_key] += 1
            
            # Fill in missing dates with 0
            trends = []
            for i in range(30):
                date = (datetime.now() - timedelta(days=29-i)).strftime("%Y-%m-%d")
                trends.append({
                    "date": date,
                    "completed_jobs": daily_counts.get(date, 0)
                })
            
            return trends
            
        finally:
            self.db.close()

