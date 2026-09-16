# EU Cost-of-Living Comparator

A small web app that answers: _"If I earn X in one European city, what salary do I need in another to maintain the same purchasing power?"_

Built while job-hunting across Europe — used it myself to compare cities I was considering for remote roles.

## 🔗 Live App

[Link coming soon — deploying shortly]

## What it does

- Select any two of 5 European cities (Berlin, Lisbon, Warsaw, Amsterdam, Dublin)
- Enter your current salary
- Instantly see the equivalent salary needed in the second city
- Visual comparison of rent and grocery costs between the two cities

## Tech Stack

- **Python** — core logic
- **pandas** — data handling and city-cost calculations
- **Streamlit** — interactive web UI
- **Eurostat API** — live EU inflation data (HICP dataset)

## Data Sources

- Rent and grocery figures: curated from public cost-of-living sources (Numbeo, Eurostat, local cost-of-living guides), current as of 2026
- Inflation trend data: live from Eurostat's public API
- Salary benchmarks: aggregated from public salary-guide sources (Morgan McKinley, Levels.fyi, industry reports)

_Note: cost-of-living figures are reasonable estimates for demonstration purposes, not precise real-time data._

## Run it locally

```bash
git clone https://github.com/YOUR_USERNAME/cost-of-living-app.git
cd cost-of-living-app
pip install -r requirements.txt
streamlit run app.py
```
