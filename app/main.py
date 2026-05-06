from fastapi import FastAPI
from app.api.routes import router
from app.database.db import create_tables

app = FastAPI(title="Content Posting Optimization System")

# Create database tables on startup
create_tables()

# Include API routes
app.include_router(router)


@app.get("/")
def home():
    return {"message": "Server running successfully"}