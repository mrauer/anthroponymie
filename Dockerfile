FROM alpine:3.7

RUN apk add --no-cache python3

WORKDIR /usr/src/app
COPY . .

RUN ["sh", "./lib/run.sh"]
