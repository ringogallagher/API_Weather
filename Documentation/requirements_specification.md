# Requirements Specification for API_Weather

## 1. Project Name
**API_Weather** – A lightweight web application that displays current weather and forecasts using an external weather API.

## 2. Stakeholders
- Repository owner (developer)
- End user viewing weather information
- System administrator
- External weather data provider

## 3. System Context
The system includes a Flask backend and a basic HTML/JS frontend. The backend fetches weather data from an external API, caches it, and returns a formatted response to the frontend.

## 4. Actors
- **Web User** – views weather information via the interface.
- **System Admin** – manages configuration and API keys.
- **External Weather API** – supplies all weather data.

## 5. System Functions (Summary)
See the Functional Requirements document. The main goal is to supply accurate, localized, and formatted weather data.

## 6. Non‑Functional Requirements
- **Performance:** API_Weather must respond within 2 seconds in 95% of requests (after caching).
- **Availability:** System should be accessible 99% of the time monthly.
- **Security:** API key must never be exposed to the frontend; it must be stored in environment variables.
- **Scalability:** System should allow adding additional data providers and horizontal scaling in the future.
- **Localization:** Must support English, Russian, and Hungarian with correct date/number formatting.

## 7. Constraints & Assumptions
- External API may limit request frequency; caching is required.
- System does not store personal user data.
- Expected deployment: VPS or PaaS.

## 8. External Interfaces
- **Weather API:** HTTP(S) REST endpoint (e.g., `/forecast.json`) with API key.
- **Configuration Files:** `.env` or `config.py` for storing keys and settings.
- **Frontend:** HTML + JavaScript calling Flask endpoints.

## 9. Acceptance Criteria
- User receives correct current weather and 3‑day forecast when entering a valid city.
- Language switching updates all text and date formats.
- Unit switching affects temperature and wind speed.
- When external API is unavailable but cached data exists, the app returns cached data with a freshness warning.
- Admin can change the API key without code modifications.

## 10. Logging & Monitoring
- All requests and errors must be logged to `logs/app.log`.
- For production deployments, external monitoring (Sentry, Prometheus) is recommended.

## 11. Testing
- Unit tests for:
  - data fetching (using mocking),
  - caching logic,
  - localization/formatting.
- Integration tests for core Flask endpoints.

## 12. Documentation & Artifacts
- `docs/requirements.md`
- `docs/uml_usecase.puml`
- Updated `README.md`
- `tests/` directory
