from app.engine.recommender import (
    generate_recommendation
)

def process_batch(batch, lookups):

    results = []

    for content in batch:

        recommendation = generate_recommendation(
            content,
            lookups
        )

        recommendation["content_id"] = (
            content["content_id"]
        )

        results.append(recommendation)

    return results