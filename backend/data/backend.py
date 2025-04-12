import pandas as pd
import matplotlib.pyplot as plt

def plot_temperature_trend():
    # Load the weather history data
    df = pd.read_csv('./data/weather_history.csv')

    # Ensure the timestamp is parsed as a datetime object
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Plot temperature over time
    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df['temperature'], label='Temperature (°C)', color='tab:blue')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trend Over Time')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./data/charts/temperature_trend.png')
    plt.show()

# Call the function to plot the graph
plot_temperature_trend()
