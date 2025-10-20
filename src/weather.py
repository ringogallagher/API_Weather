import requests

#CITY = input("Введите название города: ")
API_KEY = "e0926730d3144f10a49132901252409"
#URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&lang=ru"
URL = f"http://api.weatherapi.com/v1/current.json"
URL_FOR_FIVE_DAYS = f"http://api.weatherapi.com/v1/forecast.json"

icons = {
}
params = {
    "q": "auto:ip",
    "days":3,
    "key": API_KEY,
    "lang": "en"
}

#responce = requests.get(URL,params = params)
responce = requests.get(URL_FOR_FIVE_DAYS,params = params)
data = responce.json()

if responce.status_code == 200 and "current" in data and "forecast" in data and "location" in data:
    city = data["location"]["name"]
    country = data["location"]["country"]
    current = data["current"]

    weather_text = data["current"]["condition"]["text"]
    temp = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    pressure = data["current"]["pressure_mb"]
    wind_speed = data["current"]["wind_kph"]
    wind_dir = data["current"]["wind_dir"]
    feels_like = data["current"]["feelslike_c"]
    icon = icons.get(weather_text, "🌍")
    print("\n🌍 Погода в городе:", city)
    print("╔════════════════════════════════╗")
    print(f"🌡️  Температура:       {temp}°C")
    print(f"🤔  Ощущается как:     {feels_like}°C")
    print(f"💧  Влажность:         {humidity}%")
    print(f"💨  Ветер:             {wind_speed} км/ч ({wind_dir})")
    print(f"🔽  Давление:          {pressure} мбар")
    print("╟────────────────────────────────╢")
    print(f"{icon}  {weather_text}")
    print("╚════════════════════════════════╝\n")
    
    print(f"\nПрогноз погоды для {city} на 5 дней:\n")
    for day in data["forecast"]["forecastday"]:
        date = day["date"]
        condition = day["day"]["condition"]["text"]
        avg_temp = day["day"]["avgtemp_c"]
        max_temp = day["day"]["maxtemp_c"]
        min_temp = day["day"]["mintemp_c"]
        chance_of_rain = day["day"].get("daily_chance_of_rain", 0)
        print(f"📅 {date}: {condition}")
        print(f"🌡 Средняя: {avg_temp}°C (мин: {min_temp}°C / макс: {max_temp}°C)")
        print(f"🌧 Вероятность дождя: {chance_of_rain}%\n")

else:
    print("Ошибка:", data)
