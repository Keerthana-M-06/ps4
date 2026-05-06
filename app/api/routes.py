from fastapi import APIRouter, HTTPException

from app.database.models import (
    ContentRequest,
    RecommendationResponse,
)

from app.database.db import (
    insert_content,
    insert_recommendation,
)

from app.engine.recommender import generate_recommendation

router = APIRouter()


# ---------------------------------
# HEALTH CHECK
# ---------------------------------
@router.get("/health")
def health_check():
    return {"status": "API working"}


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