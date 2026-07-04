import requests

BASE_URL = "http://127.0.0.1:8000"


def generate_meal_plan(payload):

    response = requests.post(
        f"{BASE_URL}/generate",
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    return response.json()