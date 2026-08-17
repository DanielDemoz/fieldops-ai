# FieldOps AI

Smart scheduling, job costing, and field-service management platform for Canadian construction, HVAC, electrical, plumbing, and home-repair SMBs.

## Problem

Small field-service businesses struggle to coordinate crews, track inventory, invoice promptly, and forecast cash flow across disconnected spreadsheets and manual scheduling.

## Approach

Developed a FastAPI backend with Streamlit dashboard covering intelligent job scheduling (OR-Tools routing), GPS-aware time tracking, inventory alerts, automated PDF invoicing, and Prophet-based cash-flow forecasting. SQLite for development with PostgreSQL-ready architecture.

## Results

- Unified workflow from booking through invoicing and analytics
- Route optimization via OR-Tools vehicle routing
- Predictive cash-flow and KPI dashboards for operational decisions
- PIPEDA-compliant design positioning for Canadian SMB market

## Tech stack

Python, FastAPI, Streamlit, SQLite/PostgreSQL, OR-Tools, Prophet, scikit-learn

## How to run

```bash
git clone https://github.com/DanielDemoz/fieldops-ai.git
cd fieldops-ai
pip install -r requirements.txt
python run_demo.py
streamlit run app/dashboard.py
```

Windows shortcut: `start_dashboard.bat`

Open http://localhost:8501

## Screenshot / demo

**Interactive demo:** https://danieldemoz.github.io/fieldops-ai/demo.html

Developed by Daniel S. Demoz — asbdansi9@gmail.com | [brukdconsultancy.com](https://brukdconsultancy.com)
