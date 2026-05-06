from app.engine.scoring import calculate_score
from app.engine.scheduler import get_decision


def generate_recommendation(content, lookups):
    creator_id = content["creator_id"]
    content_type = content["content_type"]
    created_timestamp = content["created_timestamp"]

    # correct lookup keys
    creator_lookup = lookups["creator_lookup"]
    activity_lookup = lookups["activity_lookup"]
    history_lookup = lookups["history_lookup"]

    base_engagement = creator_lookup.get(creator_id, 1.0)

    best_score = -1
    best_platform = None
    best_time = None

    platforms = ["Instagram", "YouTube"]

    for platform in platforms:
        for hour in range(24):
            activity_score = activity_lookup.get((platform, hour), 0.5)

            historical_score = history_lookup.get(
                (creator_id, platform, content_type, hour),
                0.5
            )

            score = calculate_score(
                base_engagement,
                activity_score,
                historical_score
            )

            if score > best_score:
                best_score = score
                best_platform = platform
                best_time = hour

    decision = get_decision(created_timestamp, best_time)

    return {
        "platform": best_platform,
        "time_slot": best_time,
        "decision": decision
    }