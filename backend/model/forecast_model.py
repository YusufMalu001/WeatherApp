import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

def train_temperature_model():
    # Load dataset
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'weather_history.csv')
    df = pd.read_csv(data_path)

    # Drop rows with missing data
    df.dropna(inplace=True)

    # Encode categorical condition column as optional future step
    # df['weather_condition'] = df['weather_condition'].astype('category').cat.codes

    # Feature selection
    X = df[['humidity']]  # You can add more features if collected
    y = df['temperature']

    # Train/test split
    X_train, X_test, y_train, y_test = X, X, y, y  # Just for testing when you have only 1 row


    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"📊 MAE: {mae:.2f}°C")
    print(f"📈 R² Score: {r2:.2f}")

    # Save the model
    model_path = os.path.join(os.path.dirname(__file__), 'temp_model.pkl')
    joblib.dump(model, model_path)
    print(f"✅ Model saved at {model_path}")

if __name__ == "__main__":
    train_temperature_model()
