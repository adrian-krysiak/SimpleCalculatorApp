# Use the official Python 3.10 image as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Create a directory for storing results (if it doesn't exist)
RUN mkdir -p /app/data

# Set environment variable for the log file to be written to a persistent location
ENV LOG_FILE=/app/app.log

# Command to run the application
CMD ["python", "app.py", "add", "5", "10"]
