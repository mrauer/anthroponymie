FROM alpine:3.7

RUN apk add --no-cache python3 \
                       python3-dev \
                       g++ \
                       libxml2-dev \
                       libxslt-dev \
                       make

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip3 install --upgrade pip==20.3.3 && \
    pip3 install -r requirements.txt

RUN pip3 install awscli

COPY . .
