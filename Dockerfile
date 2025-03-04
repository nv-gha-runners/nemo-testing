ARG BASE_IMAGE=python:3.12-bookworm

FROM ${BASE_IMAGE}

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest"] 
