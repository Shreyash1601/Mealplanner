import streamlit as st

from api import generate_meal_plan

from styles import load_css

from components import (
    meal_card,
    grocery_list,
    substitutions,
    budget,
)

st.set_page_config(
    page_title="Smart AI Meal Planner",
    page_icon="🍽️",
    layout="wide",
)

st.markdown(load_css(), unsafe_allow_html=True)

st.title("🍽️ Smart AI Meal Planner")

st.caption("Generate personalized meal plans using AI")

with st.sidebar:

    st.header("Preferences")

    age = st.number_input(
        "Age",
        1,
        100,
        25,
    )

    cuisine = st.selectbox(
        "Cuisine",
        [
            "Indian",
            "Chinese",
            "Italian",
            "Mexican",
        ],
    )

    diet = st.selectbox(
        "Diet",
        [
            "Vegetarian",
            "Non Vegetarian",
            "Vegan",
        ],
    )

    budget_amount = st.number_input(
        "Budget (₹)",
        100,
        5000,
        500,
    )

    people = st.number_input(
        "People",
        1,
        10,
        2,
    )

    calories = st.number_input(
        "Calories Goal",
        1000,
        5000,
        2000,
    )

    cooking_time = st.slider(
        "Cooking Time",
        10,
        120,
        30,
    )

    ingredients = st.text_area(
        "Available Ingredients",
        "Rice, Tomato, Onion, Milk",
    )

    allergies = st.text_input(
        "Allergies",
        "",
    )

generate = st.button("🚀 Generate Meal Plan")

if generate:

    payload = {

        "age": age,

        "cuisine": cuisine,

        "diet": diet,

        "budget": budget_amount,

        "people": people,

        "calories": calories,

        "cooking_time": cooking_time,

        "available_ingredients": [
            i.strip()
            for i in ingredients.split(",")
            if i.strip()
        ],

        "allergies": [
            a.strip()
            for a in allergies.split(",")
            if a.strip()
        ],
    }

    with st.spinner("🤖 AI is preparing your meal plan..."):

        response = generate_meal_plan(payload)

    col1, col2, col3 = st.columns(3)

    with col1:

        meal_card(
            "🍳 Breakfast",
            response["breakfast"],
        )

    with col2:

        meal_card(
            "🍛 Lunch",
            response["lunch"],
        )

    with col3:

        meal_card(
            "🥗 Dinner",
            response["dinner"],
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        grocery_list(
            response["grocery_list"]
        )

    with right:

        substitutions(
            response["substitutions"]
        )

    st.divider()

    budget(
        response["estimated_cost"],
        response["budget_status"],
    )