# services/fin-dash/Dockerfile
FROM python:3.9
ENV MAKEFLAGS="-j1"
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir --verbose -r requirements.txt

COPY src/ /app/src

# If your main dashboard entrypoint is src/main.py:
CMD ["python", "src/main.py"]