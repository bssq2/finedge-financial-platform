FROM python:3.9

# Install build essentials & C++ toolchain for cmdstanpy (used by Prophet)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    python3-dev \
    libpython3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy & install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt

# Copy service code
COPY src/ /app/src

# Start the Flask app
CMD ["python", "src/main.py"]