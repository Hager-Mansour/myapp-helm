FROM python:3.10-alpine3.21

RUN apk update && apk upgrade --no-cache

WORKDIR /app

RUN apk add --no-cache gcc musl-dev mariadb-connector-c-dev

RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN adduser -D appuser
USER appuser

CMD ["python", "app.py"]



