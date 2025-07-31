FROM python:3.11-slim

WORKDIR /app

COPY main.py .

# WICHTIG: CMD erwartet Liste, damit Argumente korrekt übergeben werden
CMD ["python", "main.py"]
