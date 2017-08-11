FROM python:3.6.2-alpine3.6

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./udpflood.py" ]
