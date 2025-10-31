"""SQLAlchemy database models for FieldOps AI"""
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Text, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime
from database.session import Base
import enum

class JobStatus(str, enum.Enum):
    pending = "pending"
    scheduled = "scheduled"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class InvoiceStatus(str, enum.Enum):
    pending = "pending"
    sent = "sent"
    paid = "paid"
    overdue = "overdue"

class Priority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    city = Column(String)
    province = Column(String)
    postal_code = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    work_orders = relationship("WorkOrder", back_populates="customer")
    invoices = relationship("Invoice", back_populates="customer")

class Technician(Base):
    __tablename__ = "technicians"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    specialty = Column(String)  # HVAC, Electrical, Plumbing, etc.
    hourly_rate = Column(Float, default=75.0)
    home_base_lat = Column(Float)
    home_base_lng = Column(Float)
    is_active = Column(Boolean, default=True)
    rating = Column(Float, default=4.5)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    work_orders = relationship("WorkOrder", back_populates="technician")
    timesheets = relationship("Timesheet", back_populates="technician")

class WorkOrder(Base):
    __tablename__ = "work_orders"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    assigned_technician_id = Column(Integer, ForeignKey("technicians.id"))
    
    job_type = Column(String, nullable=False)  # Classification result
    description = Column(Text)
    location = Column(String, nullable=False)
    lat = Column(Float)
    lng = Column(Float)
    
    status = Column(SQLEnum(JobStatus), default=JobStatus.pending)
    priority = Column(SQLEnum(Priority), default=Priority.medium)
    
    scheduled_date = Column(DateTime)
    scheduled_start_time = Column(DateTime)
    scheduled_end_time = Column(DateTime)
    
    actual_start_time = Column(DateTime)
    actual_end_time = Column(DateTime)
    
    estimated_duration = Column(Float)  # hours
    actual_duration = Column(Float)
    
    estimated_cost = Column(Float)
    actual_cost = Column(Float)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    customer = relationship("Customer", back_populates="work_orders")
    technician = relationship("Technician", back_populates="work_orders")
    parts_used = relationship("JobPart", back_populates="work_order")
    timesheets = relationship("Timesheet", back_populates="work_order")
    invoice = relationship("Invoice", back_populates="work_order", uselist=False)

class InventoryItem(Base):
    __tablename__ = "inventory_items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    sku = Column(String, unique=True)
    category = Column(String)
    description = Column(Text)
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, default=0.0)
    reorder_level = Column(Integer, default=10)
    supplier = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    job_parts = relationship("JobPart", back_populates="inventory_item")

class JobPart(Base):
    __tablename__ = "job_parts"
    
    id = Column(Integer, primary_key=True, index=True)
    work_order_id = Column(Integer, ForeignKey("work_orders.id"))
    inventory_item_id = Column(Integer, ForeignKey("inventory_items.id"))
    
    quantity_used = Column(Integer, default=1)
    unit_cost = Column(Float)
    total_cost = Column(Float)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    work_order = relationship("WorkOrder", back_populates="parts_used")
    inventory_item = relationship("InventoryItem", back_populates="job_parts")

class Timesheet(Base):
    __tablename__ = "timesheets"
    
    id = Column(Integer, primary_key=True, index=True)
    technician_id = Column(Integer, ForeignKey("technicians.id"))
    work_order_id = Column(Integer, ForeignKey("work_orders.id"))
    
    check_in_time = Column(DateTime, nullable=False)
    check_in_lat = Column(Float)
    check_in_lng = Column(Float)
    
    check_out_time = Column(DateTime)
    check_out_lat = Column(Float)
    check_out_lng = Column(Float)
    
    hours_worked = Column(Float)
    is_verified = Column(Boolean, default=False)
    has_anomaly = Column(Boolean, default=False)
    anomaly_reason = Column(String)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    technician = relationship("Technician", back_populates="timesheets")
    work_order = relationship("WorkOrder", back_populates="timesheets")

class Invoice(Base):
    __tablename__ = "invoices"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    work_order_id = Column(Integer, ForeignKey("work_orders.id"), unique=True)
    
    invoice_number = Column(String, unique=True, nullable=False)
    invoice_date = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime)
    
    labor_hours = Column(Float, default=0.0)
    labor_rate = Column(Float, default=0.0)
    labor_cost = Column(Float, default=0.0)
    
    materials_cost = Column(Float, default=0.0)
    other_charges = Column(Float, default=0.0)
    
    subtotal = Column(Float, default=0.0)
    tax_rate = Column(Float, default=0.13)  # 13% HST for Ontario
    tax_amount = Column(Float, default=0.0)
    total_amount = Column(Float, default=0.0)
    
    status = Column(SQLEnum(InvoiceStatus), default=InvoiceStatus.pending)
    paid_date = Column(DateTime)
    
    pdf_path = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    customer = relationship("Customer", back_populates="invoices")
    work_order = relationship("WorkOrder", back_populates="invoice")

