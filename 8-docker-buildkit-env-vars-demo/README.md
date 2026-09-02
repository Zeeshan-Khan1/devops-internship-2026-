# Docker BuildKit & Environment Variables Demo

A simple Flask app containerized with Docker, used to practice core Docker
concepts during my DevOps internship at Expertflow.

## What this project demonstrates
- Building a custom Docker image from a Dockerfile
- Using BuildKit (`DOCKER_BUILDKIT=1`) for modern, layered, cached builds
- ENTRYPOINT vs CMD behavior
- Configuring containers via environment variables (`APP_ENV`, `PORT`)
- Running the same image in two different "modes" without rebuilding it

## Tech used
- Python 3.11 (slim base image)
- Flask
- Docker / BuildKit

## Project structure

.
├── app.py # Flask app
├── Dockerfile # Image build instructions
├── requirements.txt # Python dependencies
└── README.md


## How to run

Build the image:
```bash
DOCKER_BUILDKIT=1 docker build -t flask-practice:1.0 .
```

Run in default (development) mode:
```bash
docker run -d -p 5000:5000 --name flask-dev flask-practice:1.0
curl localhost:5000
```

Run in production mode by overriding environment variables:
```bash
docker run -d -p 3000:3000 -e APP_ENV=production -e PORT=3000 --name flask-prod flask-practice:1.0
curl localhost:3000
```

## Key takeaway
The same Docker image behaves differently depending on the environment
variables passed at runtime — no code changes or rebuilds needed. This is
the foundation of running one image consistently across dev, staging, and
production environments.
