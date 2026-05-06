from fastapi import APIRouter, HTTPException

from app.database.models import (
    ContentRequest,
    RecommendationResponse,
)

from app.database.db import (
    insert_content,
    insert_recommendation,
)

router = APIRouter()


# ---------------------------------
# HEALTH CHECK
# ---------------------------------
@router.get("/health")
def health_check():
    return {"status": "API working"}


# ---------------------------------
# TEMP DUMMY ENGINE FUNCTION
# PERSON 1 WILL REPLACE THIS
# ---------------------------------
def generate_recommendation(content):

    if content.content_type == "SHORT":
        platform = "Instagram"
        time_slot = 20
    else:
        platform = "YouTube"
        time_slot = 21

    decision = (
        "POST_NOW"
        if content.created_timestamp == time_slot
        else "SCHEDULE"
    )

    return {
        "content_id": content.content_id,
        "platform": platform,
        "time_slot": time_slot,
        "decision": decision,
    }


# ---------------------------------
# SUBMIT CONTENT
# ---------------------------------
@router.post(
    "/submit_content",
    response_model=RecommendationResponse,
)
def submit_content(content: ContentRequest):

    try:

        # 1. STORE CONTENT
        insert_content(content)

        # 2. GENERATE RECOMMENDATION
        recommendation = generate_recommendation(content)

        # 3. STORE RECOMMENDATION
        insert_recommendation(recommendation)

        # 4. RETURN RESPONSE
        return recommendation

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )