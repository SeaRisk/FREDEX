
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Replace 'YOUR_FRED_API_KEY' with actual FRED API key
FRED_API_KEY = '78ebaa886dab75a49844635695eb19a0'

def fetch_fred_series_data(series_id, start_date, end_date):
    """Fetches time series data from the FRED API."""
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": start_date,
        "observation_end": end_date,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()['observations']
        return [(item['date'], item['value']) for item in data if item['value'] != '.']
    else:
        print("Failed to fetch data")
        return []

def plot_data(series_data, series_id):
    """Plots time series data using Matplotlib and adds explanatory text below."""
    dates = [datetime.strptime(date, '%Y-%m-%d') for date, _ in series_data]
    values = [float(value) for _, value in series_data]

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(dates, values, marker='', color='blue', linewidth=2, label=series_id)
    ax.set_title(f'Time Series Data for {series_id}')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.tick_params(axis='x', rotation=45)
    ax.legend()
    
    # Adjust the subplot parameters to give the explanatory text more room
    plt.subplots_adjust(bottom=0.5)
    
    # Place the explanatory text below the graph
    explanation_text = """
Simplified Explanation:
Imagine a shopping cart with items like bread, milk, eggs, a T-shirt, and a movie ticket. If this cart cost $100 last year and $105 this year, the CPI helps measure how much more expensive or cheaper this cart has become. A CPI of 105 suggests a 5% price increase from the base year.

Controversies and Specific Years:
Basket of Goods: The CPI basket's composition can be controversial, as consumption patterns evolve, potentially making the basket less reflective of current consumer habits.

Substitution Effect: Traditional CPI might not fully account for consumers switching to cheaper alternatives when prices rise, possibly overstating inflation.

Housing Prices: Incorporating housing costs accurately into the CPI, including ownership and rent, remains a contentious issue.

Notable Years on the CPI Graph:
1970s Oil Price Shocks: The CPI graph shows significant spikes in inflation during the 1970s, particularly around 1973 and 1979, due to oil price shocks that drastically increased energy and transportation costs.

Early 1980s Inflation Control: Sharp CPI increases continued into the early 1980s. In response, central banks, particularly the Federal Reserve in the United States, raised interest rates significantly to combat inflation, leading to a noticeable peak in CPI around 1981-1982.

2008 Financial Crisis: The CPI graph may show a dip or a period of low inflation following the 2008 financial crisis, reflecting decreased consumer demand and a slowing economy.

"""
    plt.figtext(0.5, 0.01, explanation_text, wrap=True, horizontalalignment='center', fontsize=8, va='bottom')
    
    plt.show()

def main():
    series_id = "CPIAUCSL"  # CPI for All Urban Consumers: All Items in U.S. City Average
    start_date = "2020-01-01"
    end_date = "2023-01-01"
    series_data = fetch_fred_series_data(series_id, start_date, end_date)
    if series_data:
        plot_data(series_data, series_id)

if __name__ == "__main__":
    main()
