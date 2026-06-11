# Backend-Practice

## Project Overview

This project is a simple FastAPI application that stores and serves student data using MongoDB. It includes:

- FastAPI application under `app/`
- MongoDB controller in `app/controllers/student.py`
- Pydantic schemas in `app/schemas/student.py`
- API routes in `app/routes/student.py`
- `Dockerfile` to containerize the FastAPI app
- `docker-compose.yml` to run FastAPI and MongoDB together

## Project Structure

```
fastapi-mongo/
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── controllers/
│   │   └── student.py
│   ├── models/
│   │   └── student.py
│   ├── routes/
│   │   └── student.py
│   └── schemas/
│       └── student.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.12
- Docker
- Docker Compose

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Lokeshram12/Backend-Practice.git
cd Backend-Practice/fastapi-mongo
```

### 2. Install dependencies locally (optional)

If you want to run the app without Docker:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m app.main
```

### 3. Build the Docker image

```bash
docker compose build
```

### 4. Run the application with Docker Compose

```bash
docker compose up --build
```

This will start:

- `web`: the FastAPI application on port `8000`
- `mongo`: the MongoDB database service

Visit: `http://localhost:8000`

## Why Docker?

Docker is used to package the application and its dependencies into a portable container. This makes the app behave the same way on any host with Docker installed.

### Benefits of Docker for this project

- **Isolation:** The FastAPI app runs in its own container with the correct Python runtime.
- **Consistency:** The same container image is used for development and deployment.
- **Portability:** Anyone can run the app without installing local dependencies manually.
- **Reproducibility:** Environment and dependencies are defined in `Dockerfile` and `requirements.txt`.

## Why use the MongoDB Docker image?

The MongoDB Docker image is used so the database can run in a separate container without manual installation.

Benefits:

- No manual MongoDB installation on the host.
- Consistent MongoDB version across environments.
- Easy start/stop and isolation from the app.
- Works well with Docker Compose for multi-container setups.

## Why Docker Compose?

`docker-compose.yml` is used because this project requires both the FastAPI app and MongoDB.

Compose provides:

- **Service orchestration:** Start app and database together.
- **Networking:** The app can access MongoDB by service name `mongo`.
- **Configuration:** Environment variables are declared centrally.
- **Volumes:** MongoDB data can persist using a Docker volume.

## How the app connects to MongoDB

The app uses the environment variable `MONGO_DETAILS`.

- In Docker Compose: `mongodb://mongo:27017`
- Locally: `mongodb://localhost:27017`

This makes the app flexible for both local and containerized use.

## Important notes

- The Docker image contains only the app code and runtime, not the database data.
- MongoDB data is stored separately in the database container or volume.
- If you want to share data across machines, you need a database backup/restore strategy or a managed database service.
- For production, add authentication, backup, monitoring, and a replica set or managed database.

## Useful commands

```bash
# Build and start services
docker compose up --build

# Stop services
docker compose down

# Follow container logs
docker compose logs -f

# Rebuild only the web service
docker compose build web
```

## Why this setup is useful

This project uses Docker and Docker Compose to make the app easier to run and maintain.

- Docker ensures the app runs the same on any machine.
- Compose keeps the app and database together.
- A separate MongoDB image is cleaner and more portable than installing Mongo manually.

## Production considerations

This project is suitable for development and testing. For production, consider:

- managed MongoDB or a MongoDB replica set
- backups and restore procedures
- secure credentials and TLS
- monitoring and logging
- autoscaling the FastAPI service
