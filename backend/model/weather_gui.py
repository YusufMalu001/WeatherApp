import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.metrics import mean_absolute_error

# Example data (actual vs predicted)
actual_values = [15.5, 14.8, 16.2, 14.5]
predicted_values = [14.9, 14.5, 15.8, 14.3]

# Calculate MAE
mae = mean_absolute_error(actual_values, predicted_values)

# Create the root window
root = tk.Tk()
root.title("Weather Prediction MAE Chart")

# Create a figure and plot the data
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(actual_values, label='Actual', marker='o')
ax.plot(predicted_values, label='Predicted', marker='x')

# Add the MAE text on the chart
ax.text(1, 16, f'MAE: {mae:.2f}', fontsize=12, color='red')  # Positioning the MAE text

ax.set_xlabel('Time/Index')
ax.set_ylabel('Temperature (°C)')  # Modify this based on your data (e.g., rainfall, temperature)
ax.set_title('Actual vs Predicted Weather')
ax.legend()
ax.grid(True)

# Embed the plot into Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Place the plot in the window
canvas.get_tk_widget().pack()

# Run the Tkinter event loop
root.mainloop()
