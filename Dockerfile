ARG BASE_IMAGE=nvcr.io/nvidia/pytorch:25.02-py3

FROM ${BASE_IMAGE}

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest"] 
