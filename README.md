# Weather Prediction Using Machine Learning

## Overview

Weather forecasting plays a pivotal role across various sectors, including agriculture, transportation, energy, and event management. With accurate predictions, stakeholders can mitigate risks, optimize resource use, and make informed decisions. This project leverages Machine Learning (ML) to predict weather conditions, automates data updates through scheduling, and visualizes forecast insights via a Supaboard dashboard. It also offers a desktop GUI, optional voice-based input, and an extensible Node.js frontend.

---

## Problem Statement

### Context

Weather conditions are influenced by a multitude of variables that change rapidly. Traditional methods often fall short in adapting to these changes in real time. In this project, we:

1. Train ML models using historical weather data to forecast key metrics.
2. Set up a scheduling mechanism to ingest and update data at regular intervals.
3. Visualize the insights in a user-friendly dashboard (Supaboard).

### Content Structure

- **ML Model for Weather Forecasting**

  - Trained on historical data.
  - Predicts temperature, humidity, wind speed, and more.

- **Scheduler for Regular Updates**

  - Automatically fetches new data.
  - Updates datasets.
  - Retrains or refines models when necessary.

- **Supaboard Dashboard**

  - Displays forecasts, trends, and real-time analytics.
  - Custom visualizations and alerts.

- **Desktop GUI & Voice Input**

  - Built with Tkinter for local interaction.
  - Supports voice input using SpeechRecognition and pyttsx3.

- **Optional Node.js Frontend**

  - Interactive web interface for weather analytics.

---

## Dataset & Column Descriptions

A typical dataset used in this project includes the following columns:

| Column Name         | Description                                          |
| ------------------- | ---------------------------------------------------- |
| `date_time`         | Date and time for each measurement or forecast.      |
| `temperature`       | Air temperature (°C/°F).                             |
| `humidity`          | Relative humidity percentage (%).                    |
| `wind_speed`        | Wind speed (m/s, km/h, or mph).                      |
| `wind_direction`    | Wind direction in degrees (0–360).                   |
| `pressure`          | Atmospheric pressure in hPa.                         |
| `precipitation`     | Rainfall/snowfall amount (mm/in).                    |
| `cloud_coverage`    | Cloud cover percentage.                              |
| `weather_condition` | Description of the weather (e.g., "rainy", "clear"). |

### Output Variable:

- `forecasted_weather`: Predicted weather condition (categorical) or a key metric (e.g., temperature).

## How to Run This Project

### 1. Clone or Download the Repository

```bash
git clone https://github.com/YusufMalu001/WeatherApp.git
cd WeatherApp
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
# If not present, manually install:
pip install pandas numpy scikit-learn matplotlib seaborn SpeechRecognition pyttsx3 pyaudio requests python-dotenv
```

> For Windows users: Use `pipwin install pyaudio` if `pyaudio` fails.

### 4. Run ML Model & GUI

```bash
cd backend
python app_gui.py
```

The GUI allows users to:

- Enter humidity
- Predict temperature using a trained model
- Use voice input to provide city names

### 5. Optional: Start Backend App

```bash
python app.py  # For basic backend logic or voice-only interface
```

### 6. Train and Visualize Model

```bash
# Train the model
python data/train_model.py

# Fetch & store data
python data/data_collector.py
python data/insert_data.py

# Visualize results
python data/visualize.py
```

### 7. Launch the Dashboard

Visualizations are designed for **Supaboard**:

- Export predictions to CSV/JSON.
- Connect Supaboard to this file.
- Configure charts and filters.

---

## Voice Input Support

We use `SpeechRecognition` and `pyttsx3` to:

- Prompt user to say a city name.
- Recognize voice input via Google Speech API.

To test voice input:

```bash
python app.py
```



## Scheduling Regular Updates

Use `scheduler.py` or external tools:

```bash
python scheduler.py
```

Or set up:

- **Cron jobs** (Linux/macOS)
- **Task Scheduler** (Windows)
- **Airflow DAGs** for production

---

## Project Structure (Simplified)

```
WeatherApp/
├── fetch_weather.py             # Simple script to fetch data
├── package.json                 # Node frontend config
├── backend/
│   ├── app.py                   # Voice + CLI app
│   ├── app_gui.py               # GUI version
│   ├── scheduler.py             # Automates fetch
│   ├── .env                     # API keys/config
│   ├── api/
│   │   └── fetch_weather.py     # API logic
│   └── data/
│       ├── data_collector.py    # Get data from OpenWeather
│       ├── insert_data.py       # Insert into CSV/db
│       ├── train_model.py       # Train ML model
│       ├── visualize.py         # Graphs & plots
│       └── *.pkl                # Saved model(s)
```

---

##  Authors

- Shahedeen Tanveer
- Yusuf Mustafa Ali Malu Bhai Wala

Feel free to contribute and submit PRs!

---

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

##  Acknowledgements

- [Scikit-learn](https://scikit-learn.org/)
- [OpenWeather API](https://openweathermap.org/api)
- [SpeechRecognition Docs](https://pypi.org/project/SpeechRecognition/)
- [Supaboard](https://supaboard.io)
