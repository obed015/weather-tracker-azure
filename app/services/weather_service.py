import httpx

from app.config import Settings
from app.services.logging_service import log_info, log_error


class WeatherService:
    BASE_URL = "https://api.weatherapi.com/v1/forecast.json"

    async def get_weather(self, city: str, days: int = 3) -> dict:
        log_info(f"Fetching weather data for city: {city}")

        params = {
            "key": Settings.WEATHER_API_KEY,
            "q": city,
            "days": days,
            "aqi": "no",
            "alerts": "no",
        }

        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                response = await client.get(self.BASE_URL, params=params)
                response.raise_for_status()

                log_info(f"Weather API success for city: {city}")

                return response.json()

        except httpx.HTTPStatusError as http_err:
            log_error(
                f"HTTP error while fetching weather for {city}: "
                f"{http_err.response.status_code}"
            )
            raise

        except Exception as ex:
            log_error(
                f"Unexpected error while fetching weather for {city}: {str(ex)}"
            )
            raise
