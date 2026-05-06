import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from app.engine.recommender import generate_recommendation

lookups = {
    "creator_lookup": {
        1: 1.2
    },
    "activity_lookup": {
        ("Instagram", 10): 1.1,
        ("Instagram", 20): 1.4,
        ("YouTube", 15): 1.3
    },
    "history_lookup": {
        (1, "Instagram", "SHORT", 10): 1.5,
        (1, "Instagram", "SHORT", 20): 1.8,
        (1, "YouTube", "SHORT", 15): 1.6
    }
}

content = {
    "creator_id": 1,
    "content_type": "SHORT",
    "created_timestamp": 20
}

result = generate_recommendation(content, lookups)

print(result)