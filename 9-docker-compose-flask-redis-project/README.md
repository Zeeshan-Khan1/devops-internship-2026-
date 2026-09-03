# Docker Compose — Flask + Redis Visit Counter

A small multi-container project demonstrating Docker Compose, custom
networking, persistent volumes, and image registry push — built during
my DevOps internship at Expertflow.

## What this project demonstrates
- Running multiple containers together with Docker Compose
- Inter-container communication over a custom Docker network (by service name)
- Persistent data storage using a named volume (Redis data survives restarts)
- Building and tagging an image, then pushing it to Docker Hub

## Tech used
- Python 3.11 (Flask)
- Redis (alpine image)
- Docker Compose

## How to run

Build and start both services:
docker compose up -d --build

Check both containers are running:
docker compose ps

Visit in browser:
http://localhost:5000

Stop and remove everything (including the volume):
docker compose down -v

## Key takeaway
Two independent containers, defined in one file, communicate over a
private Docker network using just their service names — and the data
one of them holds survives even after both containers are recreated.
