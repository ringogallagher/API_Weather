from flask import Flask, render_template, request, jsonify
import requests
import datetime
import locale

app = Flask(__name__)

API_KEY = "e0926730d3144f10a49132901252409"
BASE_URL = "http://api.weatherapi.com/v1/forecast.json"

LANG_MAP = {
    "en": "en",
    "ru": "ru",
    "hu": "hu"
}

def format_date(date_str, lang):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    locales = {"ru": "ru_RU.utf8", "hu": "hu_HU.utf8", "en": "en_US.utf8"}
    try:
        locale.setlocale(locale.LC_TIME, locales.get(lang, "en_US.utf8"))
    except:
        locale.setlocale(locale.LC_TIME, "C")
    return date_obj.strftime("%d %B")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    data = request.get_json()
    lang = data.get("lang", "en")

    user_ip = request.remote_addr
    query = "auto:ip" if user_ip == "127.0.0.1" else user_ip

    params = {
        "key": API_KEY,
        "q": query,
        "days": 5,
        "lang": LANG_MAP.get(lang, "en")
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200 and "current" in data:
        current = data["current"]
        forecast = data["forecast"]["forecastday"]

        # добавляем защиту — если меньше 5, возвращаем сколько есть
        forecast = forecast[:5]

        result = {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "temp": current["temp_c"],
            "feels_like": current["feelslike_c"],
            "humidity": current["humidity"],
            "pressure": current["pressure_mb"],
            "wind_speed": current["wind_kph"],
            "wind_dir": current["wind_dir"],
            "condition": current["condition"]["text"],
            "icon": current["condition"]["icon"],
            "forecast": [
                {
                    "date": format_date(day["date"], lang),
                    "condition": day["day"]["condition"]["text"],
                    "avg_temp": day["day"]["avgtemp_c"],
                    "min_temp": day["day"]["mintemp_c"],
                    "max_temp": day["day"]["maxtemp_c"],
                    "rain": day["day"].get("daily_chance_of_rain", 0)
                }
                for day in forecast
            ]
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Weather data not available"}), 404

if __name__ == "__main__":
    app.run(debug=True)


