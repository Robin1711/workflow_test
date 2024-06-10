# Dockerfile has to be execute in the root dir
# FROM python:3.11
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    postgresql-client \
    libpq-dev \
    docker.io \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
#Install Azure CLI.
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

EXPOSE 8000

