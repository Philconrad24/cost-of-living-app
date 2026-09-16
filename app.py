import streamlit as st
import pandas as pd
from app_logic import salary_equivalent

cities = pd.read_csv("cities.csv")

st.title("EU Cost-of-Living Comparator")
st.write("If it works, you'll see this sentence in your browser.")

city_list = cities["city"].tolist()
city_a = st.selectbox("Select your current city", city_list)

city_b = st.selectbox("Select the city you're comparing to", city_list)
salary_a = st.number_input("Enter your current salary (EUR)", min_value=0, value=50000)

if st.button("Calculate"):
    result = salary_equivalent(salary_a, city_a, city_b, cities)
    st.metric(label=f"Equivalent salary in {city_b}", value=f"€{result:,.0f}")
    row_a = cities[cities["city"] == city_a].iloc[0]
    row_b = cities[cities["city"] == city_b].iloc[0]

    chart_data = pd.DataFrame({
        city_a: [row_a["avg_rent_1br_center_eur"], row_a["avg_monthly_groceries_eur"]],
        city_b: [row_b["avg_rent_1br_center_eur"], row_b["avg_monthly_groceries_eur"]]
    }, index=["Rent", "Groceries"])

    st.bar_chart(chart_data)