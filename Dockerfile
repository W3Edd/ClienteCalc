FROM python:3.9.4-alpine

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

COPY . /app
RUN apk update && apk upgrade && apk add bash
ENTRYPOINT ["/bin/bash"]
