# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir flask numpy

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables
ENV ANGLE_INCREMENT_A=0.1
ENV ANGLE_INCREMENT_B=0.05
ENV FOREGROUND_COLOR="red"
ENV BACKGROUND_COLOR="black"

# Run app.py when the container launches
CMD ["python", "app.py"]
