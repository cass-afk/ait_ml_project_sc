# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install pytest
RUN pip install pytest-depends


# Expose the port Flask will run on
EXPOSE 8080

# Set environment variables
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["python", "app.py"]
