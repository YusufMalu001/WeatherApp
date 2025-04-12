import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, r2_score

# Set the font family to DejaVu Sans (which supports more characters)
plt.rcParams["font.family"] = "DejaVu Sans"

# Load CSV
file_path = os.path.join(os.path.dirname(__file__), 'weather_history.csv')
df = pd.read_csv(file_path)
df['date_time'] = pd.to_datetime(df['date_time'])

# Output directory for charts
charts_dir = os.path.join(os.path.dirname(__file__), 'charts')
os.makedirs(charts_dir, exist_ok=True)

# Set seaborn style
sns.set(style="whitegrid")

# 1️⃣ Plot: Temperature over Time
plt.figure(figsize=(10, 4))
sns.lineplot(x='date_time', y='temperature', data=df, marker="o")
plt.title("🌡️ Temperature Over Time")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
temp_path = os.path.join(charts_dir, 'temperature_trend.png')
plt.savefig(temp_path)
print(f"✅ Saved: {temp_path}")
plt.close()

# 2️⃣ Plot: Humidity vs Temperature
plt.figure(figsize=(6, 4))
sns.scatterplot(x='humidity', y='temperature', data=df, hue='weather_condition')
plt.title("💧 Humidity vs Temperature")
plt.xlabel("Humidity (%)")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
scatter_path = os.path.join(charts_dir, 'humidity_vs_temperature.png')
plt.savefig(scatter_path)
print(f"✅ Saved: {scatter_path}")
plt.close()

# 3️⃣ Plot: Weather Condition Frequency
plt.figure(figsize=(6, 4))
sns.countplot(x='weather_condition', data=df)
plt.title("🌥️ Weather Condition Frequency")
plt.xlabel("Condition")
plt.ylabel("Count")
plt.tight_layout()
condition_path = os.path.join(charts_dir, 'weather_condition_frequency.png')
plt.savefig(condition_path)
print(f"✅ Saved: {condition_path}")
plt.close()

# Load model
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'temp_model.pkl')
model = joblib.load(model_path)

# Predict temperatures using humidity values
humidity_values = df[['humidity']].values
df['predicted_temperature'] = model.predict(humidity_values)

# Evaluate prediction
mae = mean_absolute_error(df['temperature'], df['predicted_temperature'])
r2 = r2_score(df['temperature'], df['predicted_temperature'])

# 📊 Plot: Actual vs Predicted Temperature
plt.figure(figsize=(10, 5))
plt.plot(df['date_time'], df['temperature'], label='Actual Temp', marker='o')
plt.plot(df['date_time'], df['predicted_temperature'], label='Predicted Temp', marker='x', linestyle='--')

plt.title("Actual vs Predicted Temperature")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

# 🔢 Add MAE & R² to the plot
plt.text(0.01, 0.95, f"MAE: {mae:.2f}°C\nR² Score: {r2:.2f}",
         transform=plt.gca().transAxes,
         fontsize=10,
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", edgecolor="gray"))

plt.legend()
plt.tight_layout()

# Save and Show
overlay_path = os.path.join(charts_dir, 'actual_vs_predicted.png')
plt.savefig(overlay_path)
print(f"✅ Saved: {overlay_path}")
plt.close()



