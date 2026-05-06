from fastapi import FastAPI
<<<<<<< HEAD
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
=======
from app.data.loader import load_datasets
from app.data.preprocess import create_lookup_maps
from app.workers.dispatcher import dispatch_tasks
from app.evaluator.metrics import evaluate_results

data = load_datasets()

lookups = create_lookup_maps(data)

contents = data["content"].to_dict(
    orient="records"
)

results = dispatch_tasks(contents)

print(results[:100])
metrics = evaluate_results(results)

print(metrics)
>>>>>>> 6d2a975e9064cd9c1b0fe6f28a3f56e056fabdbe
