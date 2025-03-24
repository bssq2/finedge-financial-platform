# Use a Python 3.9 base image (adjust as needed for your architecture)
FROM python:3.9

# If you have limited memory, limit parallel compilation
ENV MAKEFLAGS="-j1"

# Install system-level build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gfortran \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Upgrade pip, setuptools, and wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# --- Step 1: Pre-install build-time dependencies for Prophet ---
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

# --- Step 2: Install pystan (Prophet 1.0 depends on PyStan2) with build isolation disabled ---
RUN pip install --no-cache-dir --no-build-isolation "pystan<3"

# --- Step 3: Now install Prophet (version 1.0) with no-build-isolation ---
RUN pip install --no-cache-dir --no-build-isolation prophet==1.0

# --- Step 4: Install any other dependencies from requirements.txt if needed ---
# If your requirements.txt contains additional packages, you can run:
# RUN pip install --no-cache-dir --no-build-isolation -r requirements.txt

# Copy the source code into the container
COPY src/ /app/src

# Specify the default command to run your app
CMD ["python", "src/main.py"]