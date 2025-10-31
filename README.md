# FieldOps AI - Smart Scheduling & Job Costing Platform

A comprehensive field service management platform designed for Canadian small and medium-sized construction, HVAC, electrical, plumbing, and home-repair companies.

**Developed by [Brukd Consultancy](https://brukdconsultancy.com/) - Practical, Profitable & Responsible AI for Canadian SMBs**

PIPEDA-Compliant | CDAP Funding Eligible | Canada-based Support

## Live Demo

**View the client demonstration page:**

### Option 1: View Interactive Demo via GitHub Pages (Recommended)
Once GitHub Pages is enabled, visit:
- **Interactive Demo:** `https://danieldemoz.github.io/fieldops-ai/demo.html`

This interactive demo replicates the Streamlit dashboard experience with live charts, job scheduling, crew management, inventory tracking, financials, and analytics - all running directly in your browser!

### Option 2: Download and Open Locally
1. Click on `index.html` in the repository
2. Click the "Raw" button (top right)
3. Right-click on the page and select "Save As" to download
4. Open the downloaded `index.html` file in your web browser

### Option 3: Clone and Open
```bash
git clone https://github.com/DanielDemoz/fieldops-ai.git
cd fieldops-ai
# Then open index.html in your browser
```

The HTML demo showcases the platform's key features, workflow, and capabilities with a professional client-facing presentation.

## Overview

FieldOps AI streamlines operations from initial booking through invoicing and cash flow management. The platform automates scheduling, optimizes technician routing, tracks inventory, monitors time and attendance, and generates invoices while providing actionable financial insights.

## Key Features

### Booking & Scheduling
- Automated job intake with intelligent classification
- Optimized daily scheduling based on technician availability and location
- Route optimization to minimize travel time and maximize efficiency

### Operations Management
- Real-time technician tracking and crew management
- Inventory management with automated reorder alerts
- Time tracking with GPS verification and anomaly detection

### Financial Management
- Automated invoice generation with labor and materials costing
- Cash flow forecasting and trend analysis
- Performance metrics and KPI tracking

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

Use the provided batch file:
```bash
start_dashboard.bat
```

This automatically checks for demo data and starts the dashboard.

## Demo Company

The system includes pre-loaded sample data for demonstration purposes featuring:
- 30 sample customers
- 12 technicians across multiple specialties
- 50+ work orders with various statuses
- Inventory tracking
- Financial records and invoices

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

## Documentation

All setup instructions are included in the Getting Started section above.

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is proprietary software developed by Brukd Consultancy. All rights reserved.

## Contact

For inquiries, please contact Brukd Consultancy.
