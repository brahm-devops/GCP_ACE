FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the application code
COPY app.py .

# Install Flask
RUN pip install Flask

# Expose port 8080 for Cloud Run compatibility
EXPOSE 8080

# Run the web app
CMD ["python", "app.py"]