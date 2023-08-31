from secrets_var import api_key
import requests

import requests

url = "https://api.openweathermap.org/geo/1.0/direct"
params = {
    "q": "ville",
    "appid": api_key
}

response = requests.get(url, params=params)
data = response.json()
print(data)
