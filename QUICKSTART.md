# Quick Start Guide - FieldOps AI Demo

## 🚀 Setup (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Initialize Demo Data
```bash
python run_demo.py
```

This will:
- Create the SQLite database
- Generate sample data for **Toronto HVAC Solutions**
- Load 30 customers, 12 technicians, 50+ work orders
- Create invoices and timesheets

### 3. Launch Dashboard
```bash
streamlit run app/dashboard.py
```

The dashboard will open in your browser at `http://localhost:8501`

## 📊 What's Included in the Demo

### Sample Company: Toronto HVAC Solutions

**Technicians (12)**
- Mix of HVAC, Electrical, Plumbing, and General Repair specialists
- Realistic ratings and hourly rates ($65-$95/hr)
- Home bases distributed around Toronto

**Work Orders (50+)**
- Various job types: HVAC Repair, AC Installation, Emergency Repairs
- Mix of statuses: pending, scheduled, in_progress, completed
- Realistic locations across Toronto area

**Financial Data**
- Invoices with labor and materials costs
- Mix of paid and pending invoices
- Cash flow forecasting

**Inventory**
- HVAC parts, electrical components, tools, and supplies
- Stock levels with reorder alerts

## 🎯 Dashboard Features

1. **Scheduler Tab** - View and optimize daily technician routes
2. **Crew Management** - Technician performance metrics
3. **Inventory** - Parts tracking with low-stock alerts
4. **Financials** - Revenue trends and cash flow forecast
5. **Analytics** - KPIs and performance metrics

## 🔧 Next Steps

- Add more jobs: Modify `utils/data_generator.py`
- Customize company: Edit `config.py`
- Integrate APIs: Add Stripe, Google Maps in `services/`
- Deploy: Use Streamlit Cloud or Railway

## 📝 Notes

- Database is SQLite (file: `fieldops.db`)
- All data is synthetic for demo purposes
- PDF invoices saved in `invoices/` directory

