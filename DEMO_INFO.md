# 🏗️ FieldOps AI - Demo Company Setup

## 📊 Sample Company: Toronto HVAC Solutions

Your demo is pre-loaded with a complete sample company showing real-world field service operations.

### Company Details
- **Name**: Toronto HVAC Solutions
- **Industry**: HVAC & Electrical Services
- **Location**: Toronto, Ontario, Canada
- **Employees**: 12 Technicians
- **Base Coordinates**: 43.6532°N, -79.3832°W

### Demo Data Includes

#### 👥 30 Customers
- Mix of residential and commercial clients
- Toronto-area addresses
- Realistic contact information

#### 👷 12 Technicians
**Specialties:**
- HVAC Specialists (4)
- Electrical Technicians (3)
- Plumbing Experts (2)
- General Repair (3)

**Attributes:**
- Hourly rates: $65-$95/hr
- Ratings: 4.2-5.0 stars
- Home bases distributed across Toronto
- Active status tracking

#### 📋 50+ Work Orders
**Job Types:**
- HVAC Repair
- AC Installation
- Furnace Maintenance
- Electrical Wiring
- Duct Cleaning
- Heat Pump Service
- Emergency Repair
- Preventive Maintenance

**Status Distribution:**
- Pending: ~15%
- Scheduled: ~25%
- In Progress: ~10%
- Completed: ~50%

**Features:**
- Realistic locations across Toronto
- Priority levels (low, medium, high, urgent)
- Estimated vs actual durations
- Cost tracking

#### 📦 Inventory (40+ Items)
**Categories:**
- **HVAC Parts**: Air Filters, Thermostats, Refrigerant, Compressors, Fan Motors
- **Electrical**: Wire, Circuit Breakers, Outlets, Switches
- **Tools**: Multimeters, Screwdriver Sets, Wrenches
- **Supplies**: Duct Tape, Insulation, Solder, Pipes

**Tracking:**
- Current stock levels
- Reorder thresholds
- Supplier information
- Part usage linked to jobs

#### ⏰ Timesheets
- GPS-verified check-in/out
- Hours worked tracking
- Anomaly detection (10% flagged)
- Linkage to work orders and technicians

#### 💰 Invoices (~25)
**Status Distribution:**
- Paid: ~60%
- Pending: ~40%

**Components:**
- Labor hours and rates
- Materials costs
- Tax calculations (13% HST)
- Payment tracking
- PDF generation ready

### 📈 Key Metrics (Sample)

- **Average Travel Time**: 25 minutes
- **Jobs Per Day**: ~1.5-2.0
- **Profit Per Job**: $150-$300
- **Material Cost Variance**: 5.2%
- **Technician Utilization**: 78.5%
- **30-Day Cash Balance Forecast**: ~$12,000-$18,000

### 🎯 Dashboard Tabs

1. **📅 Scheduler**
   - Daily job assignments
   - Route optimization
   - Technician schedules
   - Job status overview

2. **👷 Crew Management**
   - Technician profiles
   - Performance metrics
   - Active job assignments
   - Rating and reviews

3. **📦 Inventory**
   - Stock levels
   - Low-stock alerts
   - Part usage tracking
   - Reorder suggestions

4. **💰 Financials**
   - Revenue trends
   - Invoice status
   - Cash flow forecasting
   - 30-day predictions

5. **📊 Analytics**
   - KPIs dashboard
   - Job completion trends
   - Performance metrics
   - Utilization stats

### 🚀 Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize demo:**
   ```bash
   python run_demo.py
   ```

3. **Launch dashboard:**
   ```bash
   streamlit run app/dashboard.py
   ```

### 💡 Features Demonstrated

✅ **NLP Booking Intake** - Classify job types from customer requests  
✅ **Smart Scheduling** - OR-Tools VRP optimization  
✅ **Parts Tracking** - Inventory management with alerts  
✅ **Time Tracking** - GPS-verified timesheets  
✅ **Auto-Invoicing** - PDF invoice generation  
✅ **Cash Flow Analytics** - Prophet-based forecasting  

### 🔧 Customization

All demo data can be customized by editing:
- `utils/data_generator.py` - Modify company name, counts, locations
- `config.py` - Change company defaults
- `database/models.py` - Add custom fields

### 📝 Notes

- Database is SQLite (`fieldops.db`)
- All data is synthetic (Faker library)
- Locations are based on Toronto coordinates
- Dates span past 30 days and next 7 days
- Perfect for demos, presentations, and testing

---

**Ready to explore?** Run `streamlit run app/dashboard.py` and start exploring Toronto HVAC Solutions!

