FROM mcr.microsoft.com/playwright/python:v1.50.0-noble
RUN apt-get update && apt-get install -y --no-install-recommends poppler-utils && rm -rf /var/lib/apt/lists/*
WORKDIR /reportflow
COPY . /reportflow
ENTRYPOINT ["python", "publication/runtime/publish.py"]
