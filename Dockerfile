ARG BASE_IMAGE=python:3.12-bookworm

FROM ${BASE_IMAGE}

RUN apt-get update && apt-get install -y \
    sudo \
    cifs-utils

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest"] 
