import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

# Load your CSV
df = pd.read_csv("weather_history.csv")

# Encoding
city_encoder = LabelEncoder()
weather_encoder = LabelEncoder()

df["city_encoded"] = city_encoder.fit_transform(df["city"])
df["weather_encoded"] = weather_encoder.fit_transform(df["weather_condition"])

# Model training (e.g., temperature ~ humidity)
X = df[["city_encoded", "humidity", "weather_encoded"]]
y = df["temperature"]

model = LinearRegression()
model.fit(X, y)

# Save model and encoders (correctly this time!)
with open("weather_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("city_encoder.pkl", "wb") as f:
    pickle.dump(city_encoder, f)

with open("weather_encoder.pkl", "wb") as f:
    pickle.dump(weather_encoder, f)

print("✅ Model and encoders trained & saved properly!")

