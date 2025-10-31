"""Scheduling and routing optimization service"""
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import math

from database.session import SessionLocal
from database.models import WorkOrder, Technician

class SchedulingService:
    """Vehicle Routing Problem (VRP) solver for technician scheduling"""
    
    def __init__(self):
        self.db = SessionLocal()
    
    def calculate_distance(self, lat1, lng1, lat2, lng2):
        """Calculate Haversine distance between two points (km)"""
        if not all([lat1, lng1, lat2, lng2]):
            return 9999.0
        
        R = 6371  # Earth radius in km
        dlat = math.radians(lat2 - lat1)
        dlng = math.radians(lng2 - lng1)
        a = (math.sin(dlat/2)**2 + 
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * 
             math.sin(dlng/2)**2)
        c = 2 * math.asin(math.sqrt(a))
        return R * c
    
    def create_distance_matrix(self, technicians: List[Technician], jobs: List[WorkOrder]):
        """Create distance matrix for VRP"""
        locations = []
        
        # Add technician home bases
        for tech in technicians:
            locations.append({
                'type': 'technician',
                'id': tech.id,
                'lat': tech.home_base_lat,
                'lng': tech.home_base_lng
            })
        
        # Add job locations
        for job in jobs:
            locations.append({
                'type': 'job',
                'id': job.id,
                'lat': job.lat,
                'lng': job.lng,
                'duration': job.estimated_duration or 2.0
            })
        
        n = len(locations)
        distance_matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    dist = self.calculate_distance(
                        locations[i]['lat'], locations[i]['lng'],
                        locations[j]['lat'], locations[j]['lng']
                    )
                    distance_matrix[i][j] = int(dist * 100)  # Convert to meters (approx)
                else:
                    distance_matrix[i][j] = 0
        
        return distance_matrix, locations
    
    def optimize_routes(self, date: datetime.date) -> Optional[Dict]:
        """Optimize technician routes for a given date"""
        try:
            # Get scheduled jobs for date
            jobs = self.db.query(WorkOrder).filter(
                WorkOrder.scheduled_date == date,
                WorkOrder.status.in_(["pending", "scheduled"])
            ).all()
            
            if not jobs:
                return {"message": "No jobs to schedule"}
            
            # Get active technicians
            technicians = self.db.query(Technician).filter(
                Technician.is_active == True
            ).all()
            
            if not technicians:
                return {"message": "No active technicians"}
            
            # Simple assignment: assign jobs to nearest technicians
            # (Full VRP would require more complex setup)
            assignments = []
            
            for job in jobs:
                if not job.lat or not job.lng:
                    continue
                
                best_tech = None
                min_distance = float('inf')
                
                for tech in technicians:
                    if not tech.home_base_lat or not tech.home_base_lng:
                        continue
                    
                    dist = self.calculate_distance(
                        tech.home_base_lat, tech.home_base_lng,
                        job.lat, job.lng
                    )
                    
                    if dist < min_distance:
                        min_distance = dist
                        best_tech = tech
                
                if best_tech:
                    job.assigned_technician_id = best_tech.id
                    job.status = "scheduled"
                    assignments.append({
                        "technician_id": best_tech.id,
                        "technician_name": best_tech.name,
                        "job_id": job.id,
                        "job_type": job.job_type,
                        "distance_km": round(min_distance, 2)
                    })
            
            self.db.commit()
            
            return {
                "date": str(date),
                "jobs_assigned": len(assignments),
                "assignments": assignments
            }
            
        except Exception as e:
            self.db.rollback()
            return {"error": str(e)}
        finally:
            self.db.close()

