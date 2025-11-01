# ============================
# 🧱 Stage 1: Builder
# ============================
FROM python:3.10-slim AS builder

# Prevent Python from writing .pyc files and using output buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set working directory
WORKDIR /app

# Install build dependencies for packages like torch/transformers
RUN apt-get update && apt-get install -y --no-install-recommends build-essential

# Copy only requirements first for caching layer
COPY requirements.txt .

# Install dependencies into a temporary directory
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt

# ============================
# 🚀 Stage 2: Final Runtime Image
# ============================
FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /install /usr/local

# Copy project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Default command to run the API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
