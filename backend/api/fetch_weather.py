# fetch_weather.py
import requests

def get_weather(city):
    API_KEY = "06c921750b9a82d8f5d1294e1586276f"  # ← Replace with your key if needed
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            print(f"❌ Error: {data.get('message')}")
            return None

        weather = {
            "city": city,
            "temperature": round(data["main"]["temp"] - 273.15, 2),
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["main"]
        }

        return weather

    except Exception as e:
        print("⚠️ API Error:", e)
        return None
