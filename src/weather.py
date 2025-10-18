import requests
from dotenv import load_dotenv
import os

load_dotenv()
CITY = input("Введите название города: ")



icons = {
}
params = {
    "q": CITY,
    "key": os.getenv("API_KEY"),
    "lang": "en"
}

response = requests.get(os.getenv("URL"),params = params)
data = response.json()

if response.status_code == 200 and "current" in data :
    weather_text = data["current"]["condition"]["text"]
    temp = data["current"]["temp_c"]
    icon = icons.get(weather_text, "🌍")
    print("\n======================")
    print(f"Погода в {CITY}")
    print("======================")
    print(f"{icon}  {weather_text}")
    print(f"🌡️  Температура: {temp}°C")
    print("======================\n")
else:
    print("Ошибка:", data)
