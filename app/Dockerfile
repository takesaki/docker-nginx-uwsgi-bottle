FROM python:3.7-alpine

COPY requirements.txt ./
RUN apk update && \
    apk --no-cache add linux-headers build-base gcc && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --no-cache-dir -r requirements.txt 

COPY uwsgi.ini ./
COPY ./src /usr/src/app
CMD uwsgi --ini uwsgi.ini
