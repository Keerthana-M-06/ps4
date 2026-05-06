import pandas as pd

def load_datasets():

    creators_df = pd.read_csv(
        "data/raw/creators.csv"
    )

    activity_df = pd.read_csv(
        "data/raw/platform_activity.csv"
    )

    history_df = pd.read_csv(
        "data/raw/historical_engagement.csv"
    )

    content_df = pd.read_csv(
        "data/raw/content.csv"
    )

    return {
        "creators": creators_df,
        "activity": activity_df,
        "history": history_df,
        "content": content_df
    }