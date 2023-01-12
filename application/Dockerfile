FROM python:3.10-alpine

WORKDIR /usr/src/application
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

COPY . .

RUN apk add --update --no-cache --virtual .tmp-build-deps \
     gcc libc-dev linux-headers postgresql-dev tree vim bash

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r req.txt