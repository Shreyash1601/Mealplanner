from pydantic import BaseModel, Field
from typing import List


class MealRequest(BaseModel):
    age: int = Field(..., gt=0)
    cuisine: str
    diet: str
    budget: int
    people: int
    calories: int
    cooking_time: int
    allergies: List[str]
    available_ingredients: List[str]


class Meal(BaseModel):
    name: str
    calories: int
    preparation_time: str
    ingredients: List[str]
    instructions: List[str]


class Substitution(BaseModel):
    ingredient: str
    substitute: str


class MealResponse(BaseModel):
    breakfast: Meal
    lunch: Meal
    dinner: Meal

    grocery_list: List[str]

    substitutions: List[Substitution]

    estimated_cost: int

    budget_status: str