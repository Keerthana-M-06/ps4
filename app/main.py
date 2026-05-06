from fastapi import FastAPI
from app.data.loader import load_datasets
from app.data.preprocess import create_lookup_maps
from app.workers.dispatcher import dispatch_tasks
from app.evaluator.metrics import evaluate_results
from app.database.db import engine
from app.database.models import Base
from app.database.db import SessionLocal
from app.database.models import Recommendation
Base.metadata.create_all(bind=engine)
db = SessionLocal()
app = FastAPI()

data = load_datasets()

lookups = create_lookup_maps(data)

contents = data["content"].to_dict(
    orient="records"
)

results = dispatch_tasks(
    contents,
    lookups
)
for result in results:

    recommendation = Recommendation(

        content_id=result["content_id"],

        platform=result.get("platform"),

        time_slot=result.get("time_slot"),

        decision=result.get("decision"),

        score=result.get("score", 0.0)
    )

    db.add(recommendation)

db.commit()
metrics = evaluate_results(results)
print(f"Total processed: {len(results)}")

print(results)

print(metrics)
db.close()