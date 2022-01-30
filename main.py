import tkinter as tk
import requests
import time
# A simple GUI that displays the metrics pertaining to the weather for any city in the world.
# Times are all presented in ET

def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=ccf25a80eb96e2151835e9d943fb5714"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    feels_like = int(json_data['main']['feels_like'] - 273.15)
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%M", time.gmtime(json_data['sys']['sunrise'] - 18000))
    sunset = time.strftime("%I:%M:%M", time.gmtime(json_data['sys']['sunset'] - 18000))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Highest temperature: " + str(max_temp) + "\n" + "Lowest temperature: " + str(min_temp) + "\n" + "Feels like: " + str(feels_like) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind: " + str(wind) + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset)

    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("arial", 10, "bold")
t = ("arial", 25, "bold")

citylabel = tk.Label(text="Please enter a city name:", font=f)
citylabel.pack()
textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
