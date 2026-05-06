from fastapi import FastAPI

app = FastAPI(
    title="Creator Content Optimization System"
)

@app.get("/")
def home():

    return {
        "message": "PS4 Backend Running"
    }