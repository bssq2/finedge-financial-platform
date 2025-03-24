# Use Python 3.9 base (ARM-compatible if on Apple Silicon or aarch64)
FROM python:3.9

# Limit parallel compilation if memory is limited
ENV MAKEFLAGS="-j1"

# Install any needed system packages (build-essentials, gfortran, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gfortran \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Set up working dir
WORKDIR /app

# Copy in your requirements
COPY requirements.txt /app/requirements.txt

# --- Force-upgrade pip, setuptools, wheel so we can build from source smoothly
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# (Recommended) Pre-install pinned numeric deps:
# - Old Prophet 1.0 tries to use PyStan2, so we pin "pystan<3".
# - Also pre-install Cython, convertdate, ephem, etc. so Prophet’s setup can import them.
RUN pip install --no-cache-dir \
    "numpy<1.24" \
    "pandas<2.0" \
    "Cython>=0.22" \
    "pystan<3" \
    convertdate ephem setuptools-git LunarCalendar holidays

# Now install everything from your original requirements,
# which presumably includes "prophet==1.0" or so:
RUN pip install --no-cache-dir --verbose -r requirements.txt

# Finally, copy your source code
COPY src/ /app/src

# Default command
CMD ["python", "src/main.py"]