# Use the official Python image as the base image with Alpine Linux
FROM python:3.12-alpine

WORKDIR /app
# Copy all your Python application files into the container
COPY ./server  /app/server
COPY ./const /app/const
COPY ./app.py /app/app.py 
COPY ./score.py /app/score.py
COPY ./utils.py /app/utils.py
COPY ./scores.txt /app/scores.txt
COPY ./resources/requirements.txt requirements.txt


# RUN apk update && apk add --no-cache build-base 

# Install required packages (e.g., Flask and other dependencies)
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip
# RUN apt install python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN ln -s /app/scores.txt  /scores.txt
RUN apk add curl

# Expose the port on which Flask server will run
# I had tried this but once I set it , I get this ERR_EMPTY_RESPONSE when calling to the docker port
# EXPOSE 8777

# Start the Flask server (modify the command as per your application)
CMD ["python", "app.py"]
