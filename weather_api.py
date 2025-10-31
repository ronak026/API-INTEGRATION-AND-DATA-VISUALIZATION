import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv('OPENWEATHER_API_KEY')  # Get API key

def fetch_weather_forecast(city):
    """Fetch 5-day/3-hour weather forecast from OpenWeatherMap API."""
    if not API_KEY:
        raise RuntimeError("API key not found. Check your .env file.")

    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = { "q": city, "appid": API_KEY, "units": "metric" }  # Set request parameters
    res = requests.get(url, params=params)  # Make API request
    return res.json()  # Return data as JSON
