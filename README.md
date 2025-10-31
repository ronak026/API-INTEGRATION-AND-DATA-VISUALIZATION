# API-INTEGRATION-AND-DATA-VISUALIZATION

"Intern ID":CT04DR535
A simple desktop app that shows a 5‑day temperature forecast for a given city using the OpenWeatherMap API. It fetches forecast data, extracts time/temperature series, and displays a line chart.

## Features

- Tkinter GUI with a city input and action button
- Fetches 5‑day/3‑hour forecast from OpenWeatherMap
- Parses timestamps and temperatures
- Visualizes temperature trend with Matplotlib + Seaborn

## Project Structure

- `main.py`: Tkinter UI and app entry point
- `weather_api.py`: API client for OpenWeatherMap forecast
- `data_processing.py`: Extracts datetime and temperature arrays
- `visualize.py`: Plots the temperature line chart
- `requirements.txt`: Python dependencies

## Prerequisites

- Python 3.9+ recommended
- An OpenWeatherMap API key (`https://openweathermap.org/api`)

## Setup

1. Clone/download the project and open the `Task-1` folder.
2. Create and activate a virtual environment (optional but recommended).
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in `Task-1` with your API key:

```bash
OPENWEATHER_API_KEY=your_api_key_here
```

## Run

From the `Task-1` directory:

```bash
python main.py
```

Enter a city (e.g., "London") and click "Show Temperature Chart" to fetch and display the forecast plot.

## Notes & Troubleshooting

- If you see: `API key not found. Check your .env file.`, ensure `.env` exists in `Task-1` and the key name is `OPENWEATHER_API_KEY`.
- If the API returns an error (e.g., city not found), the app shows a message dialog with the error reason.
- The chart window may appear behind other windows on some platforms; check your taskbar if it doesn’t pop to the front.
- Matplotlib/Seaborn require a GUI backend; on headless environments, the plot window cannot be displayed.

## License

MIT (or as applicable to your project).
