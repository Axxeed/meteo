from secrets_var import api_key
import requests

url = "https://api.openweathermap.org/geo/1.0/direct"
params = {
    "q": "Lyon",
    "appid": api_key
}

response = requests.get(url, params=params)
data = response.json()
print(data)

url_weather = "https://api.openweathermap.org/data/2.5/weather"

params_weather = {
    "lat": "xxxxxxxx",
    "lon": "xxxxxxx",
    "appid": "XXXXXXXXXX"
}

response_weather = requests.get(url_weather, params=params_weather)
data_weather = response_weather.json()

print(data_weather)
