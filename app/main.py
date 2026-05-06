from fastapi import FastAPI

from app.data.loader import load_datasets
from app.data.preprocess import create_lookup_maps

from app.workers.dispatcher import dispatch_tasks

from app.evaluator.metrics import evaluate_results

from app.database.db import (
    create_tables,
    insert_recommendation
)

app = FastAPI()

# create database tables
create_tables()

# load datasets
data = load_datasets()

# preprocess lookup maps
lookups = create_lookup_maps(data)

# content rows
contents = data["content"].to_dict(
    orient="records"
)

# process recommendations
results = dispatch_tasks(
    contents,
    lookups
)

# save recommendations
for result in results:

    insert_recommendation(result)

# metrics
metrics = evaluate_results(results)

print(f"Total processed: {len(results)}")

print(metrics)