from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import Settings
from app.db.init_db import init_db
from app.services.weather_service import WeatherService
from app.services.favourites_service import FavouritesService

app = FastAPI(title="Weather Tracker Azure")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

weather_service = WeatherService()
favourites_service = FavouritesService()


@app.on_event("startup")
async def startup_event():
    Settings.validate()
    init_db()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    favourites = favourites_service.get_all()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "weather": None,
            "error": None,
            "searched_city": "",
            "favourites": favourites,
        },
    )


@app.post("/search", response_class=HTMLResponse)
async def search_weather(request: Request, city: str = Form(...)):
    favourites = favourites_service.get_all()

    try:
        weather = await weather_service.get_weather(city)
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "weather": weather,
                "error": None,
                "searched_city": city,
                "favourites": favourites,
            },
        )
    except Exception as ex:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "weather": None,
                "error": f"Unable to retrieve weather data: {str(ex)}",
                "searched_city": city,
                "favourites": favourites,
            },
            status_code=500,
        )


@app.post("/favourites/add")
async def add_favourite(
    city_name: str = Form(...),
    country: str = Form(default="")
):
    favourites_service.add(city_name=city_name, country=country)
    return RedirectResponse(url="/", status_code=303)


@app.post("/favourites/delete/{city_id}")
async def delete_favourite(city_id: int):
    favourites_service.delete(city_id)
    return RedirectResponse(url="/", status_code=303)


@app.get("/health")
async def health():
    return {"status": "ok", "environment": Settings.APP_ENV}
