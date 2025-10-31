import tkinter as tk
from tkinter import messagebox
from weather_api import fetch_weather_forecast  # Fetch weather data from API
from data_processing import extract_time_and_temp  # Extract time & temperature info
from visualize import plot_temperature_chart  # Plot temperature chart

def get_weather():
    city = city_entry.get()  # Get user input
    if not city:
        messagebox.showinfo("Input Required", "Please enter a city name.")
        return

    data = fetch_weather_forecast(city)  # Get weather data
    if data.get('cod') != "200":  # Check if API returned success
        messagebox.showerror("API Error", f"Error: {data.get('message', 'Unknown error')}")
        return

    times, temps = extract_time_and_temp(data)  # Process weather data
    plot_temperature_chart(times, temps, city)  # Show chart

# --- GUI Setup ---
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("400x200")
root.resizable(False, False)

heading = tk.Label(root, text="Weather Dashboard", font=("Arial", 16, "bold"))
heading.pack(pady=10)

city_label = tk.Label(root, text="City Name:", font=("Arial", 12))
city_label.pack()

city_entry = tk.Entry(root, font=("Arial", 12), width=25)
city_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Show Temperature Chart", font=("Arial", 12), command=get_weather)
fetch_button.pack(pady=10)

root.mainloop()  # Run the app
