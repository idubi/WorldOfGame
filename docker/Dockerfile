# Use the official Python image as the base image with Alpine Linux
FROM python:3.8-alpine
# Set environment variables if needed
# ENV MY_VARIABLE my_value
# Set the working directory
WORKDIR /
# Copy all your Python application files into the container
COPY ../  /app


# Install required packages (e.g., Flask and other dependencies)
RUN pip3 install --upgrade pip
RUN pip install -r /app/resources/requirements.txt

# Expose the port on which your Flask server will run (change this as needed)
EXPOSE 8777

# Start the Flask server (modify the command as per your application)
CMD ["python", "./app/app.py"]
