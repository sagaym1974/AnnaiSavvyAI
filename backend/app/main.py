from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(
    title="Annai Savvy AI",
    version="0.2"
)

app.include_router(upload_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Annai Savvy AI!"
    }