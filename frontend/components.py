import streamlit as st


def meal_card(title, meal):

    st.markdown(
        f"""
<div class="meal-card">

<h2>{title}</h2>

<h3>{meal["name"]}</h3>

<p>⏱ {meal["preparation_time"]}</p>

<p>🔥 {meal["calories"]} Calories</p>

</div>

""",
        unsafe_allow_html=True,
    )

    st.write("### Ingredients")

    for ingredient in meal["ingredients"]:
        st.checkbox(
            ingredient,
            value=True,
            disabled=True,
            key=f"{title}_{ingredient}",
        )

    with st.expander("Recipe"):

        for step in meal["instructions"]:
            st.write(f"• {step}")


def grocery_list(items):

    st.subheader("🛒 Grocery List")

    for item in items:
        st.checkbox(item)


def substitutions(items):

    st.subheader("🔄 Ingredient Substitutions")

    if len(items) == 0:
        st.success("No substitutions needed.")
        return

    for sub in items:

        st.info(
            f'{sub["ingredient"]}  ➜  {sub["substitute"]}'
        )


def budget(cost, status):

    st.subheader("💰 Budget Summary")

    st.metric(
        "Estimated Cost",
        f"₹{cost}"
    )

    if "within" in status.lower():

        st.success(status)

    else:

        st.error(status)