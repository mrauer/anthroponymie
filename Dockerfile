FROM alpine:3.7

RUN apk add --no-cache python3 \
                       python3-dev \
                       g++ \
                       libxml2-dev \
                       libxslt-dev \
                       make \
                       R

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip3 install --upgrade pip==20.1.1 && \
    pip3 install -r requirements.txt

COPY . .

RUN ["sh", "./lib/run.sh"]
