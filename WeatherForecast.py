#predict weather by city NAME using https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={b0ef296da405f0c4efaef58a365024f7} API 
import requests
import json
def weather(city):
    api_key = "b0ef296da405f0c4efaef58a365024f7"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json() 
    print(x)
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature (in kelvin unit) = " +
              str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in percentage) = " +
              str(current_humidiy) +
              "\n description = " +
              str(weather_description))
    else:
        print(" City Not Found ")
weather(input("city_name:  "))