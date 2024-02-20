import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Replace 'YOUR_FRED_API_KEY' with actual FRED API key
FRED_API_KEY = ''

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
    """Plots time series data using Matplotlib."""
    dates = [datetime.strptime(date, '%Y-%m-%d') for date, _ in series_data]
    values = [float(value) for _, value in series_data]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, values, marker='', color='blue', linewidth=2, label=series_id)
    plt.title(f'Time Series Data for {series_id}')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
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
