# Functional Requirements for API_Weather

## Core Functionalities (MUST)
1. **Retrieve Current Weather** – The system must return current weather data (temperature, weather description, wind speed, humidity, pressure) for a specified location.
2. **Retrieve Weather Forecast** – The system must provide a forecast for N days (configurable, default is 3 days).
3. **Multiple Ways to Set Location** – The system must support location input by city name, coordinates (latitude/longitude), and optionally IP geolocation.
4. **Localization** – The system must support switching languages (e.g., `en`, `ru`, `hu`) for weather descriptions and date formats.
5. **Unit Selection** – The user must be able to switch between Celsius/Fahrenheit and km/h or m/s.
6. **Caching** – The system must cache the external API response for a configurable duration (e.g., 10 minutes).
7. **Error Handling** – The system must properly display network errors, API errors, and missing-data messages.
8. **Web Interface** – Provide a simple HTML interface with input fields and formatted weather output.
9. **API Key & Configuration Management** – Admin must be able to update API keys and cache settings without modifying application code.

## Additional Functionalities (SHOULD)
10. **Auto-Refresh** – The system should allow automatic refresh of data on a timer (user-defined).
11. **History Logging** – Store a log of recent weather requests for admin access.
12. **Fallback Provider** – The system should attempt using an alternative weather API if the primary provider fails.
13. **Testing** – The project should include unit tests for core modules (fetch, caching, localization, formatting).

## Optional Functionalities (COULD)
14. **Hourly Forecast** – Provide a 24-hour detailed hourly forecast.
15. **Saved Locations** – Allow users to store favorite locations in localStorage.
16. **Themes** – Support for dark/light UI themes.

## Out-of-Scope (WON'T)
17. **User Authentication** – No login or registration functionality is required at this stage.
