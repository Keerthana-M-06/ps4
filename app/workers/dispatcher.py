from app.workers.worker import process_batch

def dispatch_tasks(
    contents,
    batch_size=100
):

    batches = [

        contents[i:i+batch_size]

        for i in range(
            0,
            len(contents),
            batch_size
        )
    ]

    all_results = []

    for idx, batch in enumerate(batches):

        print(f"Processing batch {idx+1}")

        results = process_batch(batch)

        all_results.extend(results)

    return all_results