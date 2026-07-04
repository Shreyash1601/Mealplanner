from prompt import SYSTEM_PROMPT

from gemini_service import generate

from schemas import MealRequest, MealResponse


def generate_meal_plan(request: MealRequest):

    prompt = f"""
{SYSTEM_PROMPT}

User Details

Cuisine: {request.cuisine}

Diet: {request.diet}

Budget: {request.budget}

People: {request.people}

Calories Goal: {request.calories}

Cooking Time: {request.cooking_time}

Allergies:
{request.allergies}

Available Ingredients:
{request.available_ingredients}
"""

    result = generate(prompt)

    return MealResponse(**result)