"""FastAPI backend for FieldOps AI"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import API_TITLE, API_VERSION, API_PREFIX

app = FastAPI(title=API_TITLE, version=API_VERSION)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "FieldOps AI API",
        "version": API_VERSION,
        "status": "running"
    }

@app.get("/api/v1/health")
def health():
    return {"status": "healthy"}

# TODO: Add more endpoints for:
# - Booking intake
# - Job scheduling
# - Inventory management
# - Timesheet tracking
# - Invoice generation
# - Analytics

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

