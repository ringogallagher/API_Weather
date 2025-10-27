from flask import Flask, render_template, request, jsonify
import requests
import datetime
import locale
from abc import ABC, abstractmethod
from config import Config

app = Flask(__name__)

# --- Configuration ---
API_KEY = Config.WEATHER_API_KEY
BASE_URL = Config.WEATHER_API_BASE_URL
LANG_MAP = Config.LANG_MAP
REQUEST_TIMEOUT = Config.REQUEST_TIMEOUT


# --- Utility Function ---
def format_date(date_str, lang):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    locales = {"ru": "ru_RU.utf8", "hu": "hu_HU.utf8", "en": "en_US.utf8"}
    try:
        locale.setlocale(locale.LC_TIME, locales.get(lang, "en_US.utf8"))
    except:
        locale.setlocale(locale.LC_TIME, "C")
    return date_obj.strftime("%d %B")


# --- Interface (IWeatherService) ---
class IWeatherService(ABC):
    @abstractmethod
    def get_weather(self, ip: str, lang: str) -> dict:
        pass


# --- Implementation (WeatherAPIService) ---
class WeatherAPIService(IWeatherService):
    def __init__(self, api_key, base_url, lang_map, timeout):
        self.api_key = api_key
        self.base_url = base_url
        self.lang_map = lang_map
        self.timeout = timeout

    def get_weather(self, ip: str, lang: str) -> dict:
        query = "auto:ip" if ip == "127.0.0.1" else ip

        params = {
            "key": self.api_key,
            "q": query,
            "days": 5,
            "lang": self.lang_map.get(lang, "en")
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=self.timeout)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            raise ConnectionError("Request timeout: Weather service is not responding")
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Connection error: Cannot reach weather service")
        except requests.exceptions.HTTPError as e:
            raise ConnectionError(f"Weather API error: {str(e)}")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Request failed: {str(e)}")

        try:
            data = response.json()
        except ValueError:
            raise ValueError("Invalid response from weather service")

        if response.status_code == 200 and "current" in data:
            return self._parse_weather_data(data, lang)
        else:
            error_msg = data.get("error", {}).get("message", "Weather data not available")
            raise ValueError(error_msg)

    def _parse_weather_data(self, data, lang):
        current = data["current"]
        forecast = data["forecast"]["forecastday"][:5]

        return {
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


# --- Dependency Injection ---
weather_service = WeatherAPIService(API_KEY, BASE_URL, LANG_MAP, REQUEST_TIMEOUT)


# --- Flask Routes ---
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather", methods=["POST"])
def weather():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request: JSON body required"}), 400

        lang = data.get("lang", "en")
        user_ip = request.remote_addr

        result = weather_service.get_weather(user_ip, lang)
        return jsonify(result)

    except ConnectionError as e:
        return jsonify({"error": str(e)}), 503
    except ValueError as e:
        return jsonify({"error": str(e)}), 502
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)