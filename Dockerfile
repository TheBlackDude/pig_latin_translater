FROM python:3.7

WORKDIR /app

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt /app/requirements.txt

RUN pip install --quiet -r /app/requirements.txt

COPY . /app
