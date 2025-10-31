"""Configuration settings for FieldOps AI"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Database
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/fieldops.db")

# API Settings
API_TITLE = "FieldOps AI API"
API_VERSION = "1.0.0"
API_PREFIX = "/api/v1"

# ML Models
MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

# Sample Company Defaults
DEFAULT_COMPANY = {
    "name": "Toronto HVAC Solutions",
    "industry": "HVAC",
    "employee_count": 12,
    "base_location": {"lat": 43.6532, "lng": -79.3832}  # Toronto
}

