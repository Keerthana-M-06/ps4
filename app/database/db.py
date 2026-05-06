import sqlite3

DB_NAME = "content_optimizer.db"


# ---------------------------------
# DATABASE CONNECTION
# ---------------------------------
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn


# ---------------------------------
# CREATE TABLES
# ---------------------------------
def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # CONTENT TABLE
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS content (
            content_id INTEGER PRIMARY KEY,
            creator_id INTEGER,
            content_type TEXT,
            created_timestamp INTEGER
        )
        """
    )

    # RECOMMENDATION TABLE
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_id INTEGER,
            platform TEXT,
            time_slot INTEGER,
            decision TEXT
        )
        """
    )

    conn.commit()
    conn.close()


# ---------------------------------
# INSERT CONTENT
# ---------------------------------
def insert_content(content):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO content (
            content_id,
            creator_id,
            content_type,
            created_timestamp
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            content.content_id,
            content.creator_id,
            content.content_type,
            content.created_timestamp,
        ),
    )

    conn.commit()
    conn.close()


# ---------------------------------
# INSERT RECOMMENDATION
# ---------------------------------
def insert_recommendation(recommendation):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO recommendations (
            content_id,
            platform,
            time_slot,
            decision
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            recommendation["content_id"],
            recommendation["platform"],
            recommendation["time_slot"],
            recommendation["decision"],
        ),
    )

    conn.commit()
    conn.close()