from secrets_var import api_key
import requests



url = "https://api.openweathermap.org/geo/1.0/direct"
url_weather = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Lyon",
    "appid": api_key
}

def get_weather(api_key: str, params) :
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()

        latitude = data[0].get("lat")
        longitude = data[0].get("lon")

        params_weather = {
            "lat": latitude,
            "lon": longitude,
            "appid": api_key
        }

        response_weather = requests.get(url_weather, params=params_weather)
        if response_weather.status_code == 200 :
            data_weather = response_weather.json()
            return data_weather
        else :
            print(f"Error:{response_weather.status_code}")
    else :
        print(f"Error:{response.status_code}")

outpout_weather = get_weather(api_key,params)
weather_description = outpout_weather["weather"][0]["description"]
temperature_location = outpout_weather["main"]["temp"]
pressure_location = outpout_weather["main"]["pressure"]
humidity_location = outpout_weather["main"]["humidity"]
wind_speed = outpout_weather["wind"]["speed"]
print(weather_description)
