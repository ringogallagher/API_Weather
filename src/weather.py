import requests

CITY = input("Введите название города: ")
API_KEY = "e0926730d3144f10a49132901252409"
#URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&lang=ru"
URL = f"http://api.weatherapi.com/v1/current.json"

icons = {
}
params = {
    "q": CITY,
    "key": API_KEY,
    "lang": "en"
}

responce = requests.get(URL,params = params)
data = responce.json()

if responce.status_code == 200 and "current" in data :
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
