from app.workers.worker import process_batch

def dispatch_tasks(
    contents,
    lookups,
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

    for batch in batches:

        results = process_batch(
            batch,
            lookups
        )

        all_results.extend(results)

    return all_results