# FieldOps AI - Smart Scheduling & Job Costing Platform

A comprehensive field service management platform designed for small to medium-sized construction, HVAC, electrical, plumbing, and home-repair companies.

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

- [Quick Start Guide](QUICKSTART.md)
- [Demo Information](DEMO_INFO.md)
- [Troubleshooting](TROUBLESHOOTING.md)

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
