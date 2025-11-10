# API_Weather
Software Development Project

A modern weather forecast web application built with Flask, featuring multi-language support, 5-day forecasts, and beautiful animations.

## 🌟 Features

- **Real-time Weather Data**: Get current weather conditions and 5-day forecasts
- **Multi-language Support**: Available in English, Russian, and Hungarian
- **Auto-detection**: Automatically detects your location via IP
- **Beautiful UI**: Modern, responsive design with weather animations
- **Error Handling**: Comprehensive error handling for robust user experience
- **RESTful API**: Clean API endpoints for weather data

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
cd API_Weather
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API keys
# - Get WeatherAPI key from: https://www.weatherapi.com/
# - Get OpenWeatherMap key from: https://openweathermap.org/
```

5. Run the application:
```bash
cd src
python weather.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## 🧪 Testing

This project includes comprehensive pytest tests for the weather API.

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_weather.py
```

### Test Coverage

The test suite includes:
- ✅ Successful API requests
- ✅ Error handling (timeout, connection errors, invalid responses)
- ✅ Different language support
- ✅ Invalid input handling
- ✅ Edge cases and boundary conditions

## 📁 Project Structure

```
API_Weather/
├── src/
│   ├── app.py           # Simple weather API (OpenWeatherMap)
│   ├── weather.py       # Main weather application
│   ├── static/
│   │   ├── style.css    # Styling
│   │   └── script.js    # Frontend logic
│   └── templates/
│       └── index.html   # Main page
├── tests/
│   ├── __init__.py
│   └── test_weather.py  # Test suite
├── requirements.txt     # Python dependencies
├── pytest.ini          # Pytest configuration
└── README.md           # This file
```

## 🔧 API Endpoints

### GET /
Returns the main weather application page.

### POST /weather
Returns weather data for the user's location.

**Request:**
```json
{
  "lang": "en"  // Optional: "en", "ru", "hu"
}
```

**Response:**
```json
{
  "city": "Budapest",
  "country": "Hungary",
  "temp": 20.5,
  "feels_like": 22.0,
  "humidity": 65,
  "pressure": 1013.0,
  "wind_speed": 15.0,
  "wind_dir": "NW",
  "condition": "Partly cloudy",
  "icon": "https://...",
  "forecast": [...]
}
```

## 🛠️ Technologies

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Weather API**: WeatherAPI.com
- **Testing**: pytest, pytest-cov
- **Styling**: CSS3 with animations and gradients

## 🔐 Security

The application follows security best practices:

- ✅ **Environment Variables**: API keys stored in `.env` file (never committed)
- ✅ **Git Ignore**: `.env` is excluded from version control
- ✅ **Example File**: `.env.example` provides template for new users
- ✅ **Config Module**: Centralized configuration management

## ⚠️ Limitations

While the application provides a robust experience, it has certain limitations:

- ⚡ **Dependency on external APIs** — relies on WeatherAPI and OpenWeatherMap; data may be unavailable if these services experience downtime or rate limits.  
- 🌍 **IP-based location detection** — location accuracy may vary depending on the user’s network provider or VPN.  
- 📱 **Mobile optimization** — designed to be responsive, but minor visual inconsistencies may occur on some mobile devices.  
- 🕒 **Forecast update intervals** — data is refreshed upon user requests and not continuously updated in real-time.  
- 🌐 **Language support** — currently supports only English, Russian, and Hungarian; additional languages are not yet available.  
- 🔒 **No user accounts** — the app does not store user data or include authentication features.  
- 🧪 **Educational project** — developed for learning purposes and not intended for production or high-load environments.

## 🐛 Error Handling

The application includes comprehensive error handling:

- ✅ API timeouts (504 Gateway Timeout)
- ✅ Connection errors (503 Service Unavailable)
- ✅ Invalid responses (502 Bad Gateway)
- ✅ Missing data (404 Not Found)
- ✅ Invalid requests (400 Bad Request)
- ✅ Server errors (500 Internal Server Error)

## 📝 Development

### Adding New Features

1. Create a feature branch
2. Implement your changes
3. Write tests for new features
4. Run the test suite: `pytest`
5. Submit a pull request

### Code Style

- Follow PEP 8 Python style guide
- Write docstrings for functions and classes
- Add comments for complex logic

## 📄 License

This project is part of a Software Development course.

## 👥 Team

- Backend Developer
- Frontend Developer  
- Tester

## 📧 Contact

For questions or issues, please open an issue in the repository.

---

**Last Updated**: January 2024
