FROM python:3.12.2

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x app-entrypoint.sh
RUN chmod +x worker-entrypoint.sh
