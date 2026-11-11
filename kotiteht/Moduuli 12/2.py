import requests

api_key = "ba5fcd0ae1de21233a833d7748c17fff"
kaupunki = input("Anna paikkakunta: ")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": kaupunki, "appid": api_key, "units": "metric", "lang": "fi"}

data = requests.get(url, params=params).json()

print(data["weather"][0]["description"])
print(data["main"]["temp"], "°C")