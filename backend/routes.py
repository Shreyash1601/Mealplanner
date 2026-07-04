from fastapi import APIRouter

from schemas import MealRequest
from meal_planner import generate_meal_plan

router = APIRouter()


@router.get("/")
def home():
    return {"status": "running"}


@router.post("/generate")
def generate(request: MealRequest):
    return generate_meal_plan(request)