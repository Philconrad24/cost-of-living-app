import requests
import pandas as pd


def get_inflation_data(country_code):
    url = f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_manr?format=JSON&lang=EN&geo={country_code}&coicop=CP00&sinceTimePeriod=2023"

    response = requests.get(url)
    data = response.json()

    time_index = data["dimension"]["time"]["category"]["index"]
    values = data["value"]

    rows = []
    for label in time_index:
        position = time_index[label]
        value = values[str(position)]
        rows.append({"month": label, "country": country_code, "inflation_rate": value})

    return pd.DataFrame(rows)


def compare_countries(country1, country2):
    df1 = get_inflation_data(country1)
    df2 = get_inflation_data(country2)

    combined_df = pd.concat([df1, df2], ignore_index=True)

    comparison = combined_df.pivot(index="month", columns="country", values="inflation_rate")
    return comparison

def salary_equivalent(salary_a, city_a, city_b, cities_df):
    row_a = cities_df[cities_df["city"] == city_a].iloc[0]
    row_b = cities_df[cities_df["city"] == city_b].iloc[0]

    total_cost_a = row_a["avg_rent_1br_center_eur"] + row_a["avg_monthly_groceries_eur"]
    total_cost_b = row_b["avg_rent_1br_center_eur"] + row_b["avg_monthly_groceries_eur"]

    salary_b = salary_a * (total_cost_b / total_cost_a)
    return salary_b

cities = pd.read_csv("cities.csv")
result = salary_equivalent(50000, "Berlin", "Lisbon", cities)
print(result)