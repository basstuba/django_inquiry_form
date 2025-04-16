FROM python:3.13.3-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app
WORKDIR /app
COPY docker/requirements.txt /app/

RUN pip install --upgrade pip\
    && pip install --upgrade setuptools\
    && pip install --no-cache-dir -r requirements.txt

COPY . /app/