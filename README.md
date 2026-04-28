# Weather Tracker – Azure Compute, Containers, Functions, Monitoring, and CI/CD

A portfolio-grade Azure Cloud Engineer project that starts as a local FastAPI weather app and evolves into a fully deployed Azure solution using App Service, Azure Container Registry, Azure Container Instances, Azure Container Apps, Azure Functions, Application Insights, Azure Monitor, Key Vault, and GitHub Actions.

## Current phase

Phase 1 – Local project foundation and working weather MVP

## Features so far

- Search city weather
- View current weather and 3-day forecast
- Save favourite cities locally
- Responsive UI
- Health endpoint
- Environment-variable based configuration

## Stack

- Python FastAPI
- Jinja templates
- Vanilla JavaScript
- SQLite
- WeatherAPI

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# add your WeatherAPI key to .env
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## Commands

### Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```
