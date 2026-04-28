import httpx
from app.config import Settings


class WeatherService:
    BASE_URL = "https://api.weatherapi.com/v1/forecast.json"

    async def get_weather(self, city: str, days: int = 3) -> dict:
        params = {
            "key": Settings.WEATHER_API_KEY,
            "q": city,
            "days": days,
            "aqi": "no",
            "alerts": "no",
        }

        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
