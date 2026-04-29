# Weather Tracker — Azure Cloud Engineering Project

A production-style Azure cloud application designed to demonstrate real-world cloud engineering practices including compute hosting, monitoring, observability, and infrastructure deployment.

This project simulates a cloud-hosted weather platform where users can search cities, view forecast data, and store favourite locations. The system integrates Azure monitoring tools to provide telemetry, logging, and health visibility.

---

#  Project Goals

This project demonstrates hands-on Azure cloud engineering skills aligned with real-world infrastructure and DevOps practices.

Key goals:

- Deploy a Python FastAPI application to Azure
- Host cloud workloads using Azure App Service
- Implement structured logging and observability
- Integrate Azure Application Insights telemetry
- Build production-style monitoring workflows
- Prepare the system for containerization and CI/CD deployment

---

#  Technology Stack

## Application

- Python 3.12
- FastAPI
- Jinja2 Templates
- SQLite (development database)
- HTTPX (external API calls)

## Azure Services

- Azure App Service (Linux)
- Azure Application Insights
- Azure Monitor
- Azure Resource Groups

## Observability

- Azure Monitor OpenTelemetry
- Application Insights request telemetry
- Structured logging
- Health check endpoints

## DevOps & Tooling

- Azure CLI
- Git
- GitHub
- VS Code
- WSL Ubuntu

---

# 🌐 Features Implemented

- Search city weather
- View current weather and forecast
- Save favourite cities
- Health endpoint monitoring
- Azure-hosted deployment
- Application telemetry logging

---

# 🖥️ Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your WeatherAPI key
uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000

hase 2 — Azure App Service Deployment

The FastAPI weather application was deployed to Azure App Service using a Linux runtime.

Azure Resources Created
Resource Group
Linux App Service Plan
Linux Web App
Configuration

Environment variables were configured using Azure App Settings:

WEATHER_API_KEY
APP_ENV
DB_PATH
SCM_DO_BUILD_DURING_DEPLOYMENT
Startup Command
gunicorn -w 2 \
-k uvicorn.workers.UvicornWorker \
-b 0.0.0.0:8000 \
app.main:app
Deployment Method
az webapp deploy \
  --resource-group <resource-group> \
  --name <app-name> \
  --src-path app.zip \
  --type zip
Validation
curl https://<app-name>.azurewebsites.net/health

Expected:

{"status":"ok","environment":"azure-app-service"}

Phase 3 — Monitoring & Observability

Application Insights telemetry was integrated using Azure Monitor OpenTelemetry.

Features Enabled
Request logging
Performance monitoring
Health telemetry
Structured logging pipeline

Queries used:

requests
| order by timestamp desc
| take 20
traces
| order by timestamp desc
| take 20


## Phase 3.2 — Structured Logging

Structured application logging was implemented using Python logging and Azure Monitor OpenTelemetry.

### Features Implemented

- Weather API request logging
- Structured JSON context logging
- Latency measurement tracking
- Error detection logging

### Example Log Output

Weather request started | {"city": "London", "days": 3}

Weather request successful | {"city": "London", "latency_seconds": 0.42}

### Azure Log Query

```kql
traces
| order by timestamp desc
| take 20

Planned Phases

Phase 4 — Containerization (Docker)
Phase 5 — Azure Container Registry (ACR)
Phase 6 — Azure Container Instances (ACI)
Phase 7 — Azure Container Apps
Phase 8 — Azure Functions Alerts
Phase 9 — CI/CD with GitHub Actions
Phase 10 — Key Vault Integration

Project Purpose

This project is designed to simulate real-world Azure cloud engineering workflows including deployment, monitoring, logging, and infrastructure lifecycle management.
