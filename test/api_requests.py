from secrets_var import api_key
import requests

url = "https://api.openweathermap.org/geo/1.0/direct"
params = {
    "q": "Lyon",
    "appid": api_key
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    print(data)
    url_weather = "https://api.openweathermap.org/data/2.5/weather"

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
        print(data_weather)
    else :
        print(f"Error:{response_weather.status_code}")
else :
    print(f"Error:{response.status_code}")
