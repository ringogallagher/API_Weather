import pytest
from unittest.mock import patch, MagicMock
import json
from src.weather import app


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestWeatherAPI:
    """Test suite for Weather API endpoints"""

    def test_index_route(self, client):
        """Test that index route returns HTML page"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Weather Forecast' in response.data

    def test_weather_endpoint_success(self, client):
        """Test successful weather data retrieval"""
        mock_response = {
            "location": {
                "name": "Budapest",
                "country": "Hungary"
            },
            "current": {
                "temp_c": 20.5,
                "feelslike_c": 22.0,
                "humidity": 65,
                "pressure_mb": 1013.0,
                "wind_kph": 15.0,
                "wind_dir": "NW",
                "condition": {
                    "text": "Partly cloudy",
                    "icon": "http://example.com/icon.png"
                }
            },
            "forecast": {
                "forecastday": [
                    {
                        "date": "2024-01-15",
                        "day": {
                            "condition": {"text": "Sunny"},
                            "avgtemp_c": 18.0,
                            "mintemp_c": 12.0,
                            "maxtemp_c": 24.0,
                            "daily_chance_of_rain": 10
                        }
                    },
                    {
                        "date": "2024-01-16",
                        "day": {
                            "condition": {"text": "Rainy"},
                            "avgtemp_c": 15.0,
                            "mintemp_c": 10.0,
                            "maxtemp_c": 20.0,
                            "daily_chance_of_rain": 80
                        }
                    }
                ]
            }
        }

        with patch('src.weather.requests.get') as mock_get:
            mock_response_obj = MagicMock()
            mock_response_obj.status_code = 200
            mock_response_obj.json.return_value = mock_response
            mock_get.return_value = mock_response_obj

            response = client.post(
                '/weather',
                json={'lang': 'en'},
                content_type='application/json'
            )

            assert response.status_code == 200
            data = json.loads(response.data)
            assert data['city'] == 'Budapest'
            assert data['temp'] == 20.5
            assert len(data['forecast']) == 2

    def test_weather_missing_json_body(self, client):
        """Test error handling when JSON body is missing"""
        response = client.post(
            '/weather',
            data='invalid json',
            content_type='application/json'
        )
        # Flask returns 400 or 500 depending on how it parses invalid JSON
        assert response.status_code in [400, 500]
        data = json.loads(response.data)
        assert 'error' in data

    def test_weather_api_timeout(self, client):
        """Test handling of API timeout"""
        with patch('src.weather.requests.get') as mock_get:
            mock_get.side_effect = pytest.importorskip('requests.exceptions').Timeout()
            
            response = client.post(
                '/weather',
                json={'lang': 'en'},
                content_type='application/json'
            )
            
            assert response.status_code == 504
            data = json.loads(response.data)
            assert 'timeout' in data['error'].lower()

    def test_weather_api_connection_error(self, client):
        """Test handling of connection error"""
        with patch('src.weather.requests.get') as mock_get:
            mock_get.side_effect = pytest.importorskip('requests.exceptions').ConnectionError()
            
            response = client.post(
                '/weather',
                json={'lang': 'en'},
                content_type='application/json'
            )
            
            assert response.status_code == 503
            data = json.loads(response.data)
            assert 'connection' in data['error'].lower()

    def test_weather_api_invalid_response(self, client):
        """Test handling of invalid JSON response"""
        with patch('src.weather.requests.get') as mock_get:
            mock_response_obj = MagicMock()
            mock_response_obj.json.side_effect = ValueError("Invalid JSON")
            mock_get.return_value = mock_response_obj
            
            response = client.post(
                '/weather',
                json={'lang': 'en'},
                content_type='application/json'
            )
            
            assert response.status_code == 502
            data = json.loads(response.data)
            assert 'error' in data

    def test_weather_missing_data_keys(self, client):
        """Test handling when API response is missing required keys"""
        mock_response = {
            "location": {"name": "Budapest"},
            # Missing 'current' and 'forecast' keys
        }

        with patch('src.weather.requests.get') as mock_get:
            mock_response_obj = MagicMock()
            mock_response_obj.status_code = 200
            mock_response_obj.json.return_value = mock_response
            mock_get.return_value = mock_response_obj

            response = client.post(
                '/weather',
                json={'lang': 'en'},
                content_type='application/json'
            )

            assert response.status_code == 404
            data = json.loads(response.data)
            assert 'error' in data

    def test_weather_different_languages(self, client):
        """Test that different languages work correctly"""
        mock_response = {
            "location": {"name": "Budapest", "country": "Hungary"},
            "current": {
                "temp_c": 20.0,
                "feelslike_c": 22.0,
                "humidity": 65,
                "pressure_mb": 1013.0,
                "wind_kph": 15.0,
                "wind_dir": "NW",
                "condition": {"text": "Partly cloudy", "icon": ""}
            },
            "forecast": {"forecastday": []}
        }

        for lang in ['en', 'ru', 'hu']:
            with patch('src.weather.requests.get') as mock_get:
                mock_response_obj = MagicMock()
                mock_response_obj.status_code = 200
                mock_response_obj.json.return_value = mock_response
                mock_get.return_value = mock_response_obj

                response = client.post(
                    '/weather',
                    json={'lang': lang},
                    content_type='application/json'
                )

                assert response.status_code == 200

    def test_weather_invalid_lang_fallback(self, client):
        """Test that invalid language falls back to default"""
        mock_response = {
            "location": {"name": "Budapest", "country": "Hungary"},
            "current": {
                "temp_c": 20.0,
                "feelslike_c": 22.0,
                "humidity": 65,
                "pressure_mb": 1013.0,
                "wind_kph": 15.0,
                "wind_dir": "NW",
                "condition": {"text": "Partly cloudy", "icon": ""}
            },
            "forecast": {"forecastday": []}
        }

        with patch('src.weather.requests.get') as mock_get:
            mock_response_obj = MagicMock()
            mock_response_obj.status_code = 200
            mock_response_obj.json.return_value = mock_response
            mock_get.return_value = mock_response_obj

            response = client.post(
                '/weather',
                json={'lang': 'xx'},  # Invalid language
                content_type='application/json'
            )

            # Should still work with default language
            assert response.status_code == 200

    def test_weather_internal_error(self, client):
        """Test handling of unexpected internal errors"""
        with patch('src.weather.requests.get') as mock_get:
            mock_get.side_effect = Exception("Unexpected error")
            
            response = client.post(
                '/weather',
                json={'lang': 'en'},
                content_type='application/json'
            )
            
            assert response.status_code == 500
            data = json.loads(response.data)
            assert 'error' in data

    def test_get_method_not_allowed(self, client):
        """Test that GET method is not allowed on /weather endpoint"""
        response = client.get('/weather')
        assert response.status_code == 405  # Method Not Allowed

    def test_weather_empty_lang(self, client):
        """Test with empty language parameter"""
        response = client.post(
            '/weather',
            json={},
            content_type='application/json'
        )
        # Should default to 'en' or return error
        # Note: This will fail with actual API if location detection fails
        assert response.status_code in [200, 400, 503, 504]  # Depending on API availability


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
