# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /home/src

# Copy source code into container
COPY home/src /home/src

# Install system dependencies (for torch & transformers)
RUN apt-get update && apt-get install -y \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
        fastapi \
        uvicorn \
        python-multipart \
        transformers \
        torch \
        aiofiles \
        pydantic

# Expose FastAPI port
EXPOSE 8080

# Default run command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
