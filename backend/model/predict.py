import joblib
import numpy as np
from speech.voice_input import talk, take_command

def predict_temperature(humidity_value):
    model = joblib.load("model/temp_model.pkl")
    humidity_array = np.array([[humidity_value]])
    prediction = model.predict(humidity_array)
    return round(prediction[0], 2)

if __name__ == "__main__":
    talk("Please say the humidity percentage.")
    humidity_input = take_command()

    try:
        humidity = float(humidity_input)
        temperature = predict_temperature(humidity)
        result = f"The predicted temperature is {temperature} degrees Celsius."
        print(result)
        talk(result)
    except ValueError:
        print("❌ Could not convert input to number.")
        talk("Sorry, I could not understand the number.")
