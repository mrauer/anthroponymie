FROM alpine:3.7

RUN apk add --no-cache python3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip3 install --upgrade pip -r requirements.txt

COPY . .

RUN ["sh", "./lib/run.sh"]
