from fastapi import FastAPI

from app.api.routes import router
from app.database.db import create_tables

from app.data.loader import load_datasets
from app.data.preprocess import create_lookup_maps


# ---------------------------------
# LOAD DATASETS ON STARTUP
# ---------------------------------
data = load_datasets()

lookups = create_lookup_maps(data)


# ---------------------------------
# FASTAPI APP
# ---------------------------------
app = FastAPI(
    title="Content Posting Optimization System"
)


# ---------------------------------
# CREATE DATABASE TABLES
# ---------------------------------
create_tables()


# ---------------------------------
# INCLUDE ROUTES
# ---------------------------------
app.include_router(router)


# ---------------------------------
# ROOT ENDPOINT
# ---------------------------------
@app.get("/")
def home():
    return {
        "message": "Server running successfully"
    }