import matplotlib.pyplot as plt
import seaborn as sns

def plot_temperature_chart(times, temps, city):
    """Plot a 5-day temperature forecast chart for the given city."""
    sns.set_theme(style='darkgrid')  # Set chart style
    plt.figure(figsize=(12, 6))  # Chart size
    plt.plot(times, temps, marker='o', label='Temperature')  # Plot data points
    plt.title(f'5-Day Temperature Forecast for {city}')
    plt.xlabel('Date & Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)  # Rotate x-axis labels
    plt.legend()
    plt.tight_layout()
    plt.show()  # Display the chart
