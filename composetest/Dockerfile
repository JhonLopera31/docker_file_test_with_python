FROM python:3.7-alpine

## Creating working directory
WORKDIR /code

## Environments
##Define main application
ENV FLASK_APP=app.py 
# Define host
ENV FLASK_RUN=0.0.0.0

## package management for alpine
RUN apk --no-cache gcc musl-dev linux-headers

## Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#Exposing ports
EXPOSE 5000

#COPY all codes on image
COPY . .

# flask was defined in the ENV, so it will execute app.py 
CMD ["flask","run"]