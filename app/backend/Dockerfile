FROM python:3.10-alpine3.21س
RUN apk update && apk upgrade --no-cache && \
    apk add --no-cache \
    gcc \
    mariadb-connector-c-dev \
    musl-dev

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN adduser -D appuser
USER appuser

CMD ["python", "app.py"]
