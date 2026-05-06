from app.engine.recommender import generate_recommendation

def process_batch(batch, lookups):

    results = []

    for content in batch:

        result = {

            "content_id": content["content_id"],

            "platform": "Instagram",

            "time_slot": 20,

            "decision": "SCHEDULE"
        }

        results.append(result)

    return results