#!/bin/sh

until cd /app
do
    echo "Waiting for server volume..."
done

celery -A celery_app.app worker --loglevel=info --concurrency 2 -E
