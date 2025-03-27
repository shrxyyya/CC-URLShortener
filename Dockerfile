# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for MySQL
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY src/ .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Add these for Windows compatibility
RUN pip install python-dotenv

# Modify main.py to use dotenv for environment variables
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]