FROM python:3.9

ENV SETUPTOOLS_USE_DISTUTILS=stdlib
ENV MAKEFLAGS="-j1"

# Install build essentials for cmdstanpy C++ toolchain
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    python3-dev \
    libpython3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install runtime dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt

# Copy source & run
COPY src/ /app/src
CMD ["python", "src/main.py"]