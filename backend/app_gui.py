import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import joblib
import numpy as np
from speech.voice_input import take_command, talk
import pandas as pd

# Load ML model
model_path = os.path.join(os.path.dirname(__file__), "model", "temp_model.pkl")
model = joblib.load(model_path)


# Prediction function
def predict_from_humidity(humidity_input):
    try:
        # Convert the humidity input into a float value
        humidity = float(humidity_input)
        
        # Pass humidity as a pandas DataFrame
        humidity_df = pd.DataFrame([[humidity]], columns=["humidity"])

        # Predict using the model
        prediction = model.predict(humidity_df)
        
        # Display the result
        result = f"Predicted Temperature: {round(prediction[0], 2)} °C"
        result_label.config(text=result)
        talk(result)
        
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input!\n{e}")


# Voice input button
def use_voice():
    talk("Please say the humidity percentage.")
    voice_text = take_command()  # Get the voice input

    if voice_text is not None and voice_text.strip() != "":
        humidity_entry.delete(0, tk.END)
        humidity_entry.insert(0, voice_text)  # Insert the valid voice input into the entry
        predict_from_humidity(voice_text)  # Proceed with prediction
    else:
        messagebox.showerror("Error", "No valid humidity input detected from voice.")


# Chart viewer
def show_chart(chart_name):
    chart_path = os.path.join(os.path.dirname(__file__), "data", "charts", chart_name)
    if not os.path.exists(chart_path):
        messagebox.showerror("Missing Chart", f"{chart_name} not found.")
        return
    img = Image.open(chart_path)
    img = img.resize((500, 300))
    img_tk = ImageTk.PhotoImage(img)
    chart_canvas.config(image=img_tk)
    chart_canvas.image = img_tk

# GUI setup
root = tk.Tk()
root.title("🌤️ Weather Forecast GUI")
root.geometry("600x500")

tk.Label(root, text="Enter Humidity (%)", font=("Arial", 12)).pack(pady=5)
humidity_entry = tk.Entry(root, font=("Arial", 14))
humidity_entry.pack()

tk.Button(root, text="Predict", font=("Arial", 12), command=lambda: predict_from_humidity(humidity_entry.get())).pack(pady=5)
tk.Button(root, text="🎙️ Use Voice", font=("Arial", 12), command=use_voice).pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)

# Chart buttons
chart_frame = tk.Frame(root)
chart_frame.pack(pady=5)
tk.Button(chart_frame, text="📈 Temperature Trend", command=lambda: show_chart("temperature_trend.png")).grid(row=0, column=0, padx=5)
tk.Button(chart_frame, text="💧 Humidity vs Temp", command=lambda: show_chart("humidity_vs_temperature.png")).grid(row=0, column=1, padx=5)
tk.Button(chart_frame, text="☁️ Condition Count", command=lambda: show_chart("weather_condition_frequency.png")).grid(row=0, column=2, padx=5)
tk.Button(chart_frame, text="🔮 Actual vs Predicted", command=lambda: show_chart("actual_vs_predicted.png")).grid(row=0, column=3, padx=5)

# Chart display
chart_canvas = tk.Label(root)
chart_canvas.pack(pady=10)

root.mainloop()
