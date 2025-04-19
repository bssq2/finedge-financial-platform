# Use official Python 3.9 image
FROM python:3.9

# Install C++ toolchain & Python headers for cmdstanpy model build
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    python3-dev \
    libpython3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy & install Python dependencies in one shot
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt

# Bring in your service code
COPY src/ /app/src

# Launch the Flask app
CMD ["python", "src/main.py"]