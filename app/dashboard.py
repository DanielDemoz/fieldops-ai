"""Main Streamlit Dashboard for FieldOps AI"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from database.models import *
from database.session import SessionLocal, init_db
from services.analytics import AnalyticsService
from utils.data_generator import load_demo_data

# Optional import for scheduler (requires ortools)
try:
    from services.scheduler import SchedulingService
    SCHEDULER_AVAILABLE = True
except ImportError:
    SCHEDULER_AVAILABLE = False
    SchedulingService = None

# Page config
st.set_page_config(
    page_title="FieldOps AI Dashboard",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
init_db()

# Sidebar
st.sidebar.title("🏗️ FieldOps AI")
st.sidebar.markdown("### Smart Scheduler & Job-Costing Platform")

# Demo Company Info
with st.sidebar:
    st.markdown("---")
    st.markdown("### 📊 Demo Company")
    st.markdown("**Toronto HVAC Solutions**")
    st.markdown("- 12 Technicians")
    st.markdown("- 50+ Active Jobs")
    st.markdown("- HVAC & Electrical Services")

# Initialize session state
if "data_loaded" not in st.session_state:
    try:
        with st.spinner("Loading demo data..."):
            load_demo_data()
            st.session_state.data_loaded = True
    except Exception as e:
        st.warning(f"Note: {e}. Data may already be loaded.")
        st.session_state.data_loaded = True

# Main Dashboard
st.title("🏗️ FieldOps AI Dashboard")
st.markdown("**Toronto HVAC Solutions** - Real-time Operations Overview")

# Quick Stats
db = SessionLocal()
try:
    # Get stats
    jobs = db.query(WorkOrder).filter(WorkOrder.status.in_(["scheduled", "in_progress"])).all()
    technicians = db.query(Technician).count()
    invoices = db.query(Invoice).filter(Invoice.status == "pending").count()
    
    # Calculate today's revenue
    today = datetime.now().date()
    today_revenue = db.query(Invoice).filter(
        Invoice.status == "paid",
        Invoice.paid_date == today
    ).all()
    revenue = sum([inv.total_amount for inv in today_revenue])
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Active Jobs", len(jobs), delta="+3")
    
    with col2:
        st.metric("Technicians", technicians, delta="0")
    
    with col3:
        st.metric("Pending Invoices", invoices, delta="-2")
    
    with col4:
        st.metric("Today's Revenue", f"${revenue:,.2f}", delta="+12%")
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📅 Scheduler", 
        "👷 Crew Management", 
        "📦 Inventory", 
        "💰 Financials",
        "📊 Analytics"
    ])
    
    with tab1:
        st.subheader("📅 Smart Scheduler")
        
        # Date selector
        selected_date = st.date_input("Select Date", datetime.now().date())
        
        # Get scheduled jobs for selected date
        scheduled_jobs = db.query(WorkOrder).filter(
            WorkOrder.scheduled_date == selected_date,
            WorkOrder.status.in_(["scheduled", "in_progress"])
        ).all()
        
        if scheduled_jobs:
            st.write(f"**{len(scheduled_jobs)} jobs scheduled for {selected_date.strftime('%B %d, %Y')}**")
            
            # Display jobs by technician
            for tech in db.query(Technician).all():
                tech_jobs = [j for j in scheduled_jobs if j.assigned_technician_id == tech.id]
                if tech_jobs:
                    with st.expander(f"👷 {tech.name} ({len(tech_jobs)} jobs)"):
                        for job in tech_jobs:
                            st.write(f"**Job #{job.id}**: {job.job_type} at {job.location}")
                            st.write(f"- Status: {job.status}")
                            st.write(f"- Est. Duration: {job.estimated_duration} hrs")
                            if job.customer:
                                st.write(f"- Customer: {job.customer.name}")
        else:
            st.info(f"No jobs scheduled for {selected_date.strftime('%B %d, %Y')}")
        
        # Optimize Schedule Button
        if st.button("🚀 Optimize Today's Routes"):
            if not SCHEDULER_AVAILABLE:
                st.warning("⚠️ Scheduler service not available. Please install ortools: pip install ortools")
            else:
                scheduler = SchedulingService()
                with st.spinner("Optimizing routes..."):
                    result = scheduler.optimize_routes(selected_date)
                    if result:
                        st.success("✅ Routes optimized!")
                        st.json(result)
    
    with tab2:
        st.subheader("👷 Crew Management")
        
        technicians_list = db.query(Technician).all()
        
        tech_col1, tech_col2 = st.columns(2)
        
        with tech_col1:
            st.write("### Technician Overview")
            tech_data = []
            for tech in technicians_list:
                active_jobs = len([j for j in jobs if j.assigned_technician_id == tech.id])
                tech_data.append({
                    "Name": tech.name,
                    "Specialty": tech.specialty,
                    "Active Jobs": active_jobs,
                    "Rating": tech.rating if hasattr(tech, 'rating') else 4.5
                })
            
            df_tech = pd.DataFrame(tech_data)
            st.dataframe(df_tech, use_container_width=True)
        
        with tech_col2:
            st.write("### Performance Metrics")
            
            # Sample performance chart
            performance_data = {
                "Technician": [t.name for t in technicians_list[:5]],
                "Jobs Completed": [15, 12, 18, 10, 14],
                "Avg Rating": [4.8, 4.6, 4.9, 4.5, 4.7]
            }
            df_perf = pd.DataFrame(performance_data)
            
            fig = px.bar(
                df_perf, 
                x="Technician", 
                y="Jobs Completed",
                title="Jobs Completed (Last 30 Days)",
                color="Avg Rating",
                color_continuous_scale="Viridis"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("📦 Inventory & Parts Tracking")
        
        # Inventory items
        inventory = db.query(InventoryItem).all()
        
        if inventory:
            inv_data = []
            for item in inventory:
                inv_data.append({
                    "Part Name": item.name,
                    "Category": item.category,
                    "Current Stock": item.quantity,
                    "Reorder Level": item.reorder_level,
                    "Status": "🔴 Low Stock" if item.quantity <= item.reorder_level else "✅ OK"
                })
            
            df_inv = pd.DataFrame(inv_data)
            st.dataframe(df_inv, use_container_width=True)
            
            # Low stock alerts
            low_stock = [item for item in inventory if item.quantity <= item.reorder_level]
            if low_stock:
                st.warning(f"⚠️ {len(low_stock)} items need reordering!")
        else:
            st.info("No inventory items found")
    
    with tab4:
        st.subheader("💰 Financial Dashboard")
        
        # Revenue Overview
        invoices_all = db.query(Invoice).all()
        
        if invoices_all:
            # Monthly revenue
            monthly_revenue = {}
            for inv in invoices_all:
                if inv.invoice_date:
                    month_key = inv.invoice_date.strftime("%Y-%m")
                    if month_key not in monthly_revenue:
                        monthly_revenue[month_key] = 0
                    if inv.status == "paid":
                        monthly_revenue[month_key] += inv.total_amount
            
            if monthly_revenue:
                df_rev = pd.DataFrame([
                    {"Month": k, "Revenue": v} 
                    for k, v in sorted(monthly_revenue.items())
                ])
                
                fig = px.line(
                    df_rev, 
                    x="Month", 
                    y="Revenue",
                    title="Monthly Revenue Trend",
                    markers=True
                )
                fig.update_traces(line_color="#1f77b4")
                st.plotly_chart(fig, use_container_width=True)
            
            # Invoice status breakdown
            status_counts = {}
            for inv in invoices_all:
                status_counts[inv.status] = status_counts.get(inv.status, 0) + 1
            
            if status_counts:
                fig_pie = px.pie(
                    values=list(status_counts.values()),
                    names=list(status_counts.keys()),
                    title="Invoice Status Distribution"
                )
                st.plotly_chart(fig_pie, use_container_width=True)
        
        # Cash Flow Forecast
        st.write("### 💹 Cash Flow Forecast")
        analytics = AnalyticsService()
        forecast = analytics.generate_cash_flow_forecast(days=30)
        
        if forecast:
            df_forecast = pd.DataFrame(forecast)
            fig_forecast = px.line(
                df_forecast,
                x="date",
                y="predicted_balance",
                title="30-Day Cash Flow Forecast",
                labels={"predicted_balance": "Predicted Balance ($)", "date": "Date"}
            )
            fig_forecast.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="Breakeven")
            st.plotly_chart(fig_forecast, use_container_width=True)
            
            # Alert if negative
            min_balance = df_forecast["predicted_balance"].min()
            if min_balance < 0:
                st.error(f"⚠️ Warning: Predicted cash gap of ${abs(min_balance):,.2f} in next 30 days")
    
    with tab5:
        st.subheader("📊 Analytics & KPIs")
        
        analytics = AnalyticsService()
        kpis = analytics.calculate_kpis()
        
        if kpis:
            st.write("### Key Performance Indicators")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Avg Travel Time",
                    f"{kpis.get('avg_travel_time', 0):.1f} min"
                )
                st.metric(
                    "Jobs Per Day",
                    f"{kpis.get('jobs_per_day', 0):.1f}"
                )
            
            with col2:
                st.metric(
                    "Profit Per Job",
                    f"${kpis.get('profit_per_job', 0):,.2f}"
                )
                st.metric(
                    "Material Cost Variance",
                    f"{kpis.get('material_variance', 0):.1f}%"
                )
            
            with col3:
                st.metric(
                    "Technician Utilization",
                    f"{kpis.get('utilization', 0):.1f}%"
                )
                st.metric(
                    "30-Day Cash Balance",
                    f"${kpis.get('cash_balance_30d', 0):,.2f}"
                )
            
            # Job completion trends
            st.write("### Job Completion Trends")
            completion_data = analytics.get_job_completion_trends()
            
            if completion_data:
                df_completion = pd.DataFrame(completion_data)
                fig = px.bar(
                    df_completion,
                    x="date",
                    y="completed_jobs",
                    title="Daily Jobs Completed (Last 30 Days)"
                )
                st.plotly_chart(fig, use_container_width=True)
        
finally:
    db.close()

st.markdown("---")
st.markdown("### 🏗️ FieldOps AI v1.0")
st.markdown("Smart scheduling, intelligent routing, automated invoicing, and cash-flow analytics for field service operations.")

