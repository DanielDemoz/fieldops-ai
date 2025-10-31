"""Quick start script for FieldOps AI Demo"""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from database.session import init_db
from utils.data_generator import load_demo_data

def main():
    print("Initializing FieldOps AI Demo...")
    print("=" * 50)
    
    # Initialize database
    print("\nCreating database...")
    init_db()
    print("Database initialized")
    
    # Load demo data
    print("\nLoading demo company data...")
    load_demo_data()
    print("Demo data loaded successfully!")
    
    print("\n" + "=" * 50)
    print("Demo setup complete!")
    print("\nTo start the dashboard, run:")
    print("   py -m streamlit run app/dashboard.py")
    print("\nDemo Company: Toronto HVAC Solutions")
    print("   - 12 Technicians")
    print("   - 50+ Work Orders")
    print("   - Inventory Tracking")
    print("   - Financial Analytics")
    print("=" * 50)

if __name__ == "__main__":
    main()

