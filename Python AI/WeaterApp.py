import tkinter as tk
import requests

def get_weather():
    city = entry.get()
    try:
        data = requests.get(f"https://wttr.in/{city}?format=3").text
        label.config(text=data)
    except Exception as e:
        label.config(text="Error fetching data")

root = tk.Tk()
root.title("Weather App - МАК")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
btn.pack(pady=5)

label = tk.Label(root, font=("Arial", 14))
label.pack(pady=10)

root.mainloop()