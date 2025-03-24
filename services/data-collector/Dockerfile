# services/data-collector/Dockerfile
FROM python:3.9

# Limit parallel builds for lower memory usage
ENV MAKEFLAGS="-j1"

# Install system libs needed to compile numeric libs / PyStan / Prophet
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy & install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --verbose -r requirements.txt

# Copy your application code
COPY src/ /app/src

CMD ["python", "src/main.py"]