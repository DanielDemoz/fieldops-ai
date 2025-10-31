# 🚀 Start FieldOps AI Dashboard

## Quick Start

### Option 1: Using Batch File (Windows)
Double-click `start_dashboard.bat`

### Option 2: Using Command Line

1. **First time setup** (only needed once):
   ```bash
   py run_demo.py
   ```

2. **Start the dashboard**:
   ```bash
   py -m streamlit run app/dashboard.py
   ```

### Option 3: If `py` doesn't work, try:
```bash
python -m streamlit run app/dashboard.py
```
or
```bash
streamlit run app/dashboard.py
```

## 📍 Access the Dashboard

Once Streamlit starts, open your browser to:
**http://localhost:8501**

## ✅ Verification

- ✅ Demo data loaded (30 customers, 12 technicians, 50+ jobs)
- ✅ Database initialized
- ✅ All dependencies installed

## 🐛 Troubleshooting

**If you get "Connection Refused":**
1. Make sure Streamlit is actually running (check the terminal output)
2. Wait a few seconds for Streamlit to fully start
3. Try refreshing the browser
4. Check if port 8501 is already in use

**If you get import errors:**
```bash
py -m pip install streamlit pandas plotly sqlalchemy faker python-dotenv pydantic
```

**If port 8501 is busy:**
Streamlit will automatically try port 8502, 8503, etc. Check the terminal output for the actual URL.

## 📊 What You'll See

The dashboard includes:
- **Scheduler Tab**: Daily job assignments
- **Crew Management**: Technician profiles
- **Inventory**: Parts tracking
- **Financials**: Revenue and cash flow
- **Analytics**: KPIs and metrics

---

**Demo Company**: Toronto HVAC Solutions

