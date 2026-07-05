# Dockerizing VayuWatch (backend & frontend) - quick reference

This document provides example Dockerfiles and a docker-compose snippet to run the backend (FastAPI + Uvicorn) and frontend (Vite / static build).

## Backend Dockerfile (example)

Use this to build a portable backend image. It assumes your project root contains `requirements.txt`, `main.py`, model files (`delhi_lstm_model.h5`, `scaler.pkl`) and other source files.

```Dockerfile
FROM python:3.11-slim
WORKDIR /app

# system deps (if needed)
RUN apt-get update && apt-get install -y build-essential --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Notes:
- If you depend on `tensorflow`, the image will grow large; consider using a smaller inference runtime or a separate model-serving container.
- Copy model files (`.h5`, `scaler.pkl`) into the image, or mount them at runtime with a volume.

## Frontend Dockerfile (example - build + serve static)

```Dockerfile
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Change the `dist` path if your Vite output directory differs.

## docker-compose (simple example)

```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
      # mount model files if you don't bake them into the image
      - ./backend/delhi_lstm_model.h5:/app/delhi_lstm_model.h5:ro
      - ./backend/scaler.pkl:/app/scaler.pkl:ro
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/aqi_db

  frontend:
    build: ./vayuwatch-frontend/vayuwatch-frontend
    ports:
      - "3000:80"

  # optional: Postgres service (example)
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=aqi_db
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

## Build & run

Run from the repo root where `docker-compose.yml` lives:

```bash
docker compose build
docker compose up
```

## Tips
- If TensorFlow is heavy, consider exposing the model as a separate microservice (TensorFlow Serving or a small Flask/FASTAPI wrapper) and keep the API container lightweight.
- Add `--no-cache` or multi-stage builds to reduce image size.

--
Add or tell me any preferences (single container vs multi-service, GPU support, or registry publishing) and I can generate actual `Dockerfile` and `docker-compose.yml` files for the workspace.
