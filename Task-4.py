import http.client
import json
import tkinter as tk
from tkinter import messagebox

def get_weather_data(location):
    # API key for OpenWeatherMap
    api_key = "YOUR_API_KEY"

    # Connect to the OpenWeatherMap API
    conn = http.client.HTTPSConnection("api.openweathermap.org")

    # Send a GET request to the API
    conn.request("GET", f"/data/2.5/weather?q={location}&appid={api_key}&units=metric")

    # Get the response from the API
    response = conn.getresponse()

    # Read the response data
    data = response.read().decode('utf-8')

    # Convert the response to JSON format
    weather_data = json.loads(data)

    # Close the connection
    conn.close()

    return weather_data

def display_weather():
    # Get the location from the entry field
    location = location_entry.get()

    try:
        # Get the weather data based on the user's input
        weather_data = get_weather_data(location)

        if 'main' in weather_data and 'weather' in weather_data:
            # Extract relevant weather information from the API response
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            description = weather_data['weather'][0]['description']

            # Display the weather information to the user
            messagebox.showinfo("Weather Information", f"Temperature: {temperature}°C\n"
                                                       f"Humidity: {humidity}%\n"
                                                       f"Wind Speed: {wind_speed} m/s\n"
                                                       f"Description: {description}")
        else:
            messagebox.showerror("Error", "Weather data not available for the specified location.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Weather Forecast")
window.configure(bg='black')
window.geometry("400x200")

# Create a label and an entry field for the location
location_label = tk.Label(window, text="Location:", fg='white', bg='black', font=("Arial", 14))
location_label.pack()
location_entry = tk.Entry(window, font=("Arial", 12))
location_entry.pack()

# Create a button to get the weather information
get_weather_button = tk.Button(window, text="Get Weather", font=("Arial", 12), command=display_weather)
get_weather_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()
