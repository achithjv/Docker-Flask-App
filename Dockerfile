# Use official Python base image
FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Copy all files from current folder to /app in container
COPY . .

# Install Flask
RUN pip install flask

# Run the application
CMD ["python", "app.py"]
