from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = "71b3b4ac915b12fa8731a2995a4c75d4"

@app.route("/weather/<city>")
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    r = requests.get(url).json()
    return jsonify(r)

if __name__ == "__main__":
    app.run(debug=True)