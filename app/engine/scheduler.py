def get_decision(created_timestamp, best_time_slot):
    if created_timestamp == best_time_slot:
        return "POST_NOW"
    else:
        return "SCHEDULE"