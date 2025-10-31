import datetime

def extract_time_and_temp(api_data):
    """
    Extract datetime and temperature data from OpenWeatherMap API response.
    Returns two lists: times (datetime objects) and temps (temperatures).
    """
    times, temps = [], []

    # Loop through each forecast entry in the API data
    for entry in api_data.get('list', []):
        # Convert UNIX timestamp to readable datetime
        times.append(datetime.datetime.fromtimestamp(entry['dt']))
        # Extract temperature value
        temps.append(entry['main']['temp'])

    return times, temps  # Return lists of times and temps
