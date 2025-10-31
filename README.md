# FieldOps AI - Smart Scheduling & Job Costing Platform

A comprehensive field service management platform designed for Canadian small and medium-sized construction, HVAC, electrical, plumbing, and home-repair companies.

**Developed by [Brukd Consultancy](https://brukdconsultancy.com/) - Practical, Profitable & Responsible AI for Canadian SMBs**

PIPEDA-Compliant | CDAP Funding Eligible | Canada-based Support

## Live Demo

**View the interactive demo:** [https://danieldemoz.github.io/fieldops-ai/demo.html](https://danieldemoz.github.io/fieldops-ai/demo.html)

Experience the full dashboard with live charts, job scheduling, crew management, inventory tracking, financials, and analytics.

## Overview

FieldOps AI streamlines operations from initial booking through invoicing and cash flow management. The platform automates scheduling, optimizes technician routing, tracks inventory, monitors time and attendance, and generates invoices while providing actionable financial insights.

## Key Features

- **Intelligent Scheduling** - Automated job scheduling with route optimization
- **Time & Attendance Tracking** - GPS-verified time tracking with anomaly detection
- **Inventory Management** - Parts tracking with automated reorder alerts
- **Automated Invoicing** - Professional invoice generation with PDF export
- **Cash Flow Analytics** - Predictive forecasting and trend analysis
- **Performance Metrics** - Comprehensive KPIs and analytics dashboard

## Technology Stack

- **Backend**: Python, FastAPI
- **Frontend**: Streamlit
- **Database**: SQLite (development), PostgreSQL (production)
- **Optimization**: OR-Tools for vehicle routing
- **Analytics**: Prophet for forecasting, scikit-learn for ML models

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/DanielDemoz/fieldops-ai.git
cd fieldops-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the demo database:
```bash
python run_demo.py
```

4. Start the dashboard:
```bash
streamlit run app/dashboard.py
```

The dashboard will be available at `http://localhost:8501`

### Quick Start (Windows)

```bash
start_dashboard.bat
```

## Project Structure

```
fieldops-ai/
├── app/                 # Streamlit dashboard application
├── api/                 # FastAPI backend endpoints
├── database/            # Database models and session management
├── services/            # Business logic services
├── utils/               # Utility functions and data generation
└── config.py           # Configuration settings
```

## License

This project is proprietary software developed by Brukd Consultancy. All rights reserved.

## Contact

For inquiries, please contact [Brukd Consultancy](https://brukdconsultancy.com/).
