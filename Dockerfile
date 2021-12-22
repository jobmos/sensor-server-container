#syntax=docker/dockerfile:1

FROM python:3.7-alpine

RUN apk update && apk upgrade
RUN apk add g++ python3-dev
# See https://archlinuxarm.org/forum/viewtopic.php?p=64598#p64598
RUN CFLAGS="-fcommon" pip3 install RPi.GPIO
RUN pip3 install adafruit-circuitpython-dht

RUN pip3 install mysql-connector-python

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-u", "-m", "flask", "run", "--host=0.0.0.0" ]
