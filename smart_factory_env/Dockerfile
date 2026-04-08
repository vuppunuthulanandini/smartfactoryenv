
# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all project files into container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Set environment variables for OpenEnv (to be configured before inference)
ENV API_BASE_URL=""
ENV MODEL_NAME=""
ENV HF_TOKEN=""

# Expose port if needed (e.g., for web UI or API)
EXPOSE 7860

# Default command to run the inference script
CMD ["python", "inference.py"]