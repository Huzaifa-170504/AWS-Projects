FROM python:3.10

# Set working directory
WORKDIR /app

# Copy everything into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port your Flask app runs on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
