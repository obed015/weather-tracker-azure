import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_ENV = os.getenv("APP_ENV", "local")
    APP_PORT = int(os.getenv("APP_PORT", "8000"))
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
    DB_PATH = os.getenv("DB_PATH", "weather.db")

    @classmethod
    def validate(cls) -> None:
        if not cls.WEATHER_API_KEY:
            raise ValueError(
                "WEATHER_API_KEY is not set. Create a .env file from .env.example."
            )
