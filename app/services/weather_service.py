import time
import httpx

from app.config import Settings
from app.services.logging_service import log_info, log_error


class WeatherService:
    BASE_URL = "https://api.weatherapi.com/v1/forecast.json"

    async def get_weather(self, city: str, days: int = 3) -> dict:
        start_time = time.time()

        log_info(
            "Weather request started",
            {"city": city, "days": days}
        )

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

                elapsed = round(time.time() - start_time, 2)

                log_info(
                    "Weather request successful",
                    {
                        "city": city,
                        "days": days,
                        "status_code": response.status_code,
                        "latency_seconds": elapsed,
                    },
                )

                return response.json()

        except httpx.HTTPStatusError as http_err:
            elapsed = round(time.time() - start_time, 2)

            log_error(
                "Weather API HTTP error",
                {
                    "city": city,
                    "days": days,
                    "status_code": http_err.response.status_code,
                    "latency_seconds": elapsed,
                },
            )

            raise

        except Exception as ex:
            elapsed = round(time.time() - start_time, 2)

            log_error(
                "Weather request unexpected error",
                {
                    "city": city,
                    "days": days,
                    "error": str(ex),
                    "latency_seconds": elapsed,
                },
            )

            raise
