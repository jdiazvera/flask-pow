FROM python:alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

RUN chmod +x gunicorn.sh
ENTRYPOINT ["./gunicorn.sh"]
