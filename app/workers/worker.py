def process_batch(batch):

    results = []

    for content in batch:

        result = {
            "content_id": content["content_id"],
            "creator_id": content["creator_id"],
            "status": "processed"
        }

        results.append(result)

    return results