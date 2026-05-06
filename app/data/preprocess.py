def create_lookup_maps(data):

    creator_lookup = {}
    activity_lookup = {}
    history_lookup = {}

    # creators
    for _, row in data["creators"].iterrows():

        creator_lookup[
            row["creator_id"]
        ] = row["base_engagement"]

    # platform activity
    for _, row in data["activity"].iterrows():

        key = (
            row["platform"],
            row["time_slot"]
        )

        activity_lookup[key] = row["activity_score"]

    # historical engagement
    for _, row in data["history"].iterrows():

        key = (
            row["creator_id"],
            row["platform"],
            row["content_type"],
            row["time_slot"]
        )

        history_lookup[key] = row["avg_engagement"]

    return {
        "creator_lookup": creator_lookup,
        "activity_lookup": activity_lookup,
        "history_lookup": history_lookup
    }