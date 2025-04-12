import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv("weather_history.csv")

# Drop duplicates and NaNs
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Convert datetime
df['date_time'] = pd.to_datetime(df['date_time'])
df['hour'] = df['date_time'].dt.hour

# Encode city and condition
le_city = LabelEncoder()
le_weather = LabelEncoder()

df['city_enc'] = le_city.fit_transform(df['city'])
df['weather_enc'] = le_weather.fit_transform(df['weather_condition'])

# Features and target
X = df[['temperature', 'humidity', 'hour', 'city_enc']]
y = df['weather_enc']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, 'weather_model.pkl')
joblib.dump(le_city, 'city_encoder.pkl')
joblib.dump(le_weather, 'weather_encoder.pkl')

print("✅ Model trained and saved!")
