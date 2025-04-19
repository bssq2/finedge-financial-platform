FROM python:3.9

# Force stdlib distutils (avoid "msvccompiler" import on Linux)
ENV SETUPTOOLS_USE_DISTUTILS=stdlib

# Limit parallel builds
ENV MAKEFLAGS="-j1"

# Install system-level build tools + python dev + distutils
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gfortran \
    cmake \
    python3-distutils \
    python3-dev \
    libpython3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Upgrade pip, setuptools, wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# --- Step 1: Pre-install build-time deps for Prophet (PyStan needs these) ---
RUN pip install --no-cache-dir \
    "numpy<1.24" \
    "pandas<2.0" \
    "Cython>=0.22" \
    convertdate \
    ephem \
    setuptools-git \
    LunarCalendar \
    holidays \
    tqdm \
    matplotlib>=2.0.0

# --- Step 2: Install PyStan2 (Prophet 1.0 depends on PyStan <3) with no build isolation ---
RUN pip install --no-cache-dir --no-build-isolation "pystan<3"

# --- Step 3: Install Prophet (1.0) with no build isolation ---
RUN pip install --no-cache-dir --no-build-isolation prophet==1.0

# --- Step 4: Install the rest of your dependencies from requirements.txt ---
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --no-build-isolation -r /app/requirements.txt

COPY src/ /app/src

CMD ["python", "src/main.py"]