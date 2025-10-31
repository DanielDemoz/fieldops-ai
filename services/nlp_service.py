"""NLP service for job classification from customer requests"""
import re
from typing import Dict

class NLPBookingService:
    """Simple NLP-based booking intake and job classification"""
    
    def __init__(self):
        # Job type keywords for classification
        self.job_keywords = {
            "HVAC Repair": ["hvac", "heating", "cooling", "air conditioning", "ac", "furnace", "air conditioner"],
            "AC Installation": ["install", "installation", "new ac", "new air conditioner", "replace ac"],
            "Furnace Maintenance": ["furnace", "maintenance", "service", "tune-up", "inspection"],
            "Electrical Wiring": ["electrical", "wiring", "outlet", "circuit", "breaker", "electrical repair"],
            "Duct Cleaning": ["duct", "vent", "air duct", "cleaning"],
            "Heat Pump Service": ["heat pump", "pump service", "pump repair"],
            "Emergency Repair": ["emergency", "urgent", "broken", "not working", "no heat", "no ac"],
            "Preventive Maintenance": ["preventive", "maintenance", "inspection", "check-up"]
        }
        
        # Urgency keywords
        self.urgency_keywords = {
            "urgent": ["emergency", "urgent", "immediately", "asap", "broken", "not working"],
            "high": ["soon", "today", "tomorrow", "important"],
            "medium": ["next week", "when available", "scheduled"],
            "low": ["whenever", "flexible", "no rush"]
        }
    
    def classify_job_type(self, text: str) -> str:
        """Classify job type from customer request text"""
        text_lower = text.lower()
        scores = {}
        
        for job_type, keywords in self.job_keywords.items():
            score = sum([1 for keyword in keywords if keyword in text_lower])
            if score > 0:
                scores[job_type] = score
        
        if scores:
            return max(scores, key=scores.get)
        return "General Repair"
    
    def extract_priority(self, text: str) -> str:
        """Extract urgency/priority from text"""
        text_lower = text.lower()
        
        for priority, keywords in self.urgency_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                return priority
        
        return "medium"
    
    def extract_location(self, text: str) -> Dict:
        """Extract location information (simplified)"""
        # Look for postal codes (Canadian format: A1A 1A1)
        postal_match = re.search(r'\b[A-Z]\d[A-Z]\s?\d[A-Z]\d\b', text.upper())
        postal_code = postal_match.group(0).replace(" ", "") if postal_match else None
        
        # Look for Toronto area mentions
        location = None
        if "toronto" in text.lower():
            location = "Toronto, ON"
        elif "downtown" in text.lower():
            location = "Downtown Toronto, ON"
        
        return {
            "postal_code": postal_code,
            "location": location or "Toronto, ON"
        }
    
    def process_booking_request(self, text: str) -> Dict:
        """Process a customer booking request and extract structured data"""
        job_type = self.classify_job_type(text)
        priority = self.extract_priority(text)
        location_info = self.extract_location(text)
        
        return {
            "job_type": job_type,
            "priority": priority,
            "location": location_info.get("location"),
            "postal_code": location_info.get("postal_code"),
            "original_text": text
        }

