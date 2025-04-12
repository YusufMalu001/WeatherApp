import os
import csv
from datetime import datetime
from speech.voice_input import take_command, talk
from api.fetch_weather import get_weather

CSV_FILE = "data/weather_history.csv"

def collect_data():
    talk("Please say the name of the city.")
    city = take_command()

    if not city or "sorry" in city.lower():
        talk("Sorry, I couldn't hear the city name. Please try again.")
        return

    weather = get_weather(city)

    if weather is None:
        talk("Weather data not found.")
        return

    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        weather['city'],
        weather['temperature'],
        weather['humidity'],
        weather['condition']
    ]

    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["date_time", "city", "temperature", "humidity", "weather_condition"])
        writer.writerow(row)

    print("✅ Weather data saved:", row)
    talk("Weather data collected and saved successfully.")

if __name__ == "__main__":
    collect_data()
