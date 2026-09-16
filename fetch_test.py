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

df_de = get_inflation_data("DE")
print(df_de.head())


df_fr = get_inflation_data("FR")

def compare_countries(country1, country2):
    df1 = get_inflation_data(country1)
    df2 = get_inflation_data(country2)

    combined_df = pd.concat([df1, df2], ignore_index=True)

    comparison = combined_df.pivot(index="month", columns="country", values="inflation_rate")
    return comparison

result = compare_countries("DE", "PT")
print(result.tail())