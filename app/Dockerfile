FROM alpine:3.10

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN apk --no-cache add --virtual build-dependencies \
      build-base \
      py-mysqldb \
      gcc \
      libc-dev \
      libffi-dev \
      mariadb-dev \
      && pip install -qq -r requirements.txt \
      && rm -rf .cache/pip \
      && apk del build-dependencies

RUN apk add --no-cache mariadb-dev build-base

EXPOSE 8000

ENTRYPOINT ["./gunicorn.sh"]
