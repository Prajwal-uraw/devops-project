Overview

This project demonstrates a simple but complete local CI/CD pipeline using Jenkins, Docker, docker-compose and pytest.
It contains two lightweight Python microservices (service1 and service2) and an automated pipeline that builds, tests and deploys them whenever changes are pushed.

The goal is to provide a clear, reproducible DevOps workflow suitable for learning, experimentation, academic assessment and local testing.

Repository Structure

dev/
├── jenkins/                     # Jenkins pipeline definitions (Jenkinsfile)
├── service1/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── service2/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── tests/
│   ├── test_service1.py
│   ├── test_service2.py
│   └── results/
│       └── report.xml           # JUnit XML test results
│
├── docker-compose.yml           # Orchestration for both microservices
├── README.md
└── .pytest_cache/               # Pytest cache (auto-generated)


Requirements

Before running the project, make sure you have:

Docker Desktop or Docker Engine

docker-compose

Python 3.8+ (only required if running tests manually)

Jenkins LTS installed locally

cURL or a browser for endpoint testing

Running the Microservices Locally

From the project folder:

1. Build the images
docker-compose build

2. Start both services
docker-compose up -d

3. Check if services are running
curl http://localhost:5001
curl http://localhost:5002


Expected outputs:

Service1 → “Welcome to service 1”

Service2 → “Welcome to service 2”

4. Stop all running containers
docker-compose down

Running Tests (pytest)

You can run tests manually with:

pytest tests/ --junitxml=tests/results/report.xml


Test output will be saved in:

tests/results/report.xml


These reports are used by Jenkins when parsing results inside the CI pipeline.

Jenkins CI/CD Pipeline

The project includes a Jenkinsfile inside:

jenkins/

Pipeline Stages

Checkout code from GitHub

Build Docker images for service1 and service2

Run pytest (JUnit XML saved to tests/results/report.xml)

Deploy using docker-compose

Smoke test endpoints using curl

Archive logs and test reports

To set up Jenkins:

Create a Pipeline job

Point it to your repository

In Jenkins → Manage Plugins → Install:

Docker plugin

Pipeline plugin

Make sure the Jenkins user can run Docker commands

If Jenkins is running on Windows or WSL, ensure Docker is running and accessible.

Rollback Strategy

A simple rollback mechanism is used for this local project:

Identify previous working Docker image tags

Update docker-compose.yml to reference the older tag

Redeploy:

docker-compose down
docker-compose up -d


Although simple, this is enough for a demonstration.
In production, rollback would be handled using:

AWS ECR image versions

ECS deployment history

Blue/Green deployments

Project Purpose

This project was created for academic evaluation of DevOps concepts, focusing on:

CI/CD workflow

Containerization

Automated testing

Pipeline orchestration

Local vs cloud deployment comparison

It also serves as a learning foundation for migrating the same pipeline to AWS using CodePipeline, CodeBuild and ECS/Fargate.

Contributors

Member 1 — Jenkins configuration, repo setup

Member 2 — service1 & Dockerfile

Member 3 — service2, pytest test suite

Notes

.pytest_cache/ is automatically generated and safe to ignore.

Jenkins logs and console outputs should be used as evidence for the report.

XML test reports should be included in the appendix.