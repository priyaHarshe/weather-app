#import required modules
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

#Funtion to get weather information form Openweathermap API
def get_weather(city):
    API_Key = "e06c1aa420d107549b8a1ac567de2b0e"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    # Parse the response JSON to get weather information
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp']-273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # Get the icon URL and return all the information
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

# Function to search weather for a city
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    #if the city is found unpack the weather information 
    icon_url, temperature, description, city , country = result
    location_label.configure(text=f"{city},{country}")

    #Get the weather icon image from the URL and update the icon label
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # Update the temperature and description labels
    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")

# Function to show info about PM Accelerator
def show_info():
    info_text = (
        "PM Accelerator is a professional service company that provides specialized "
        "project management training and consulting services. We help organizations "
        "achieve their business goals by delivering tailored project management solutions.\n\n"
        "The Product Manager Accelerator Program is designed to support PM professionals "
        "through every stage of their career. From students looking for entry-level jobs to "
        "Directors looking to take on a leadership role, our program has helped over hundreds "
        "of students fulfill their career aspirations.\n\n"
        "Our Product Manager Accelerator community is ambitious and committed. Through our program, "
        "they have learned, honed, and developed new PM and leadership skills, giving them a strong foundation "
        "for their future endeavors."
    )
    messagebox.showinfo("About PM Accelerator", info_text)

    
# Create the main window
root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

# Entry widget -> to enter the city name
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)


# Button widget -> to search to search for weather information
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# Label widget ->to show city/country name
location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

# Label widget -> to show weather icon
icon_label = tk.Label(root)
icon_label.pack()

#Label widget -> to show the temperature 
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

#Label widget -> to show the weather description 
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

# Label to show your name
name_label = tk.Label(root, text="Developed by Priya Harshe", font="Helvetica, 15")
name_label.pack(pady=20)

# Button widget -> to show info about PM Accelerator
info_button = ttkbootstrap.Button(root, text="Info", command=show_info, bootstyle="info")
info_button.pack(pady=10)


# Start the GUI main loop
root.mainloop()