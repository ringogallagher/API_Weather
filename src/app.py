from flask import Flask, jsonify
import requests
from config import Config

app = Flask(__name__)

# Load API key from environment
API_KEY = Config.OPENWEATHER_API_KEY

@app.route("/weather/<city>")
def get_weather(city):
    url = f"{Config.OPENWEATHER_API_BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=ru"
    r = requests.get(url).json()
    return jsonify(r)

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)