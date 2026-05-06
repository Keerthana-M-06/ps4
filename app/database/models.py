from pydantic import BaseModel


# ---------------------------
# CONTENT REQUEST MODEL
# ---------------------------
class ContentRequest(BaseModel):
    content_id: int
    creator_id: int
    content_type: str
    created_timestamp: int


# ---------------------------
# RECOMMENDATION RESPONSE MODEL
# ---------------------------
class RecommendationResponse(BaseModel):
    content_id: int
    platform: str
    time_slot: int
    decision: str