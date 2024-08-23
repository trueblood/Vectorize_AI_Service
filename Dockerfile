# Use an official TensorFlow runtime as a parent image (includes Python and TensorFlow)
FROM tensorflow/tensorflow:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

COPY .env /app/.env

# Install virtualenv and create a virtual environment
RUN pip install virtualenv
RUN virtualenv venv

# Set environment variables from .env file
ENV API_KEY=
ENV PORT=8080

# Install any needed packages specified in requirements.txt using the virtual environment
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 8080

# Define environment variable to ensure TensorFlow model runs in the non-interactive mode
ENV TF_CPP_MIN_LOG_LEVEL=2

# Run app.py when the container launches, using the virtual environment
CMD ["venv/bin/python", "app.py"]




FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

COPY .env /app/.env

# Set environment variables from .env file
ENV API_KEY=
ENV PORT=8080

EXPOSE 8080
CMD ["python", "app.py"]