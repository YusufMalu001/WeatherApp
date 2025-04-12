import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

def train_temperature_model():
    df = pd.read_csv("../data/weather_data.csv")
    df.dropna(inplace=True)

    X = df[['humidity', 'wind_speed', 'pressure', 'cloud_coverage']]
    y = df['temperature']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    score = r2_score(y_test, predictions)
    print(f"✅ Temperature Prediction Accuracy: {score * 100:.2f}%")

    plt.plot(y_test.values, label="Actual")
    plt.plot(predictions, label="Predicted")
    plt.title("Original vs Predicted Temperature")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    train_temperature_model()
