import tkinter as tk
import urllib.request
import urllib.parse
import json
import time 

def getWeather(_event=None):
    city = textfield.get()   # user must type: City,CountryCode (e.g Harare,ZW)
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + urllib.parse.quote(city) + "&appid=06c921750b9a82d8f5d1294e1586276f"
    
    with urllib.request.urlopen(api) as response:
        json_data = json.load(response)
    
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']))
    
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\nMax Temp: " + str(max_temp) + "\nMin Temp: " + str(min_temp) + "\nPressure: " + str(pressure) + "\nHumidity: " + str(humidity) + "\nWind Speed: " + str(wind) + "\nSunrise: " + sunrise + "\nSunset: " + sunset
    
    label1.config(text=final_info)
    label2.config(text=final_data)
    

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()

textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()

label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()
