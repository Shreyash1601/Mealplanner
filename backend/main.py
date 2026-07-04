from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Smart Meal Planner API",
    version="1.0"
)

app.include_router(router)