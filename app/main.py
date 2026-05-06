from fastapi import FastAPI
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
