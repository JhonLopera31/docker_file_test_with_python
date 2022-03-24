FROM python:3.8.13-alpine3.14

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["pyhon","/app/main.py" ]