import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Application configuration"""
    
    # API Keys
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
    
    # API URLs
    WEATHER_API_BASE_URL = "http://api.weatherapi.com/v1/forecast.json"
    OPENWEATHER_API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    # Flask configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    
    # Request settings
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))
    
    # Language settings
    LANG_MAP = {
        "en": "en",
        "ru": "ru",
        "hu": "hu"
    }
    
    @staticmethod
    def validate():
        """Validate that required configuration is present"""
        errors = []
        
        if not Config.WEATHER_API_KEY:
            errors.append("WEATHER_API_KEY is not set in environment variables")
        
        if not Config.OPENWEATHER_API_KEY:
            errors.append("OPENWEATHER_API_KEY is not set in environment variables")
        
        if errors:
            raise ValueError("\n".join(errors))
        
        return True
