FROM python:3.12-slim

RUN useradd -s /bin/bash -d /app app
RUN mkdir -p /app && chown -R app:app /app

ENV PORT=8000 \
    GUNICORN_THREADS=8 \
    GUNICORN_WORKERS=2 \
    GUNICORN_TIMEOUT=0 \
    GUNICORN_APP_MODULE=app.wsgi \
    PYTHONUNBUFFERED=1

USER app
WORKDIR /app
RUN python3 -m venv env
RUN env/bin/pip install --no-cache-dir --upgrade pip && env/bin/pip install pip-tools
ADD requirements.txt .
RUN env/bin/pip install --no-cache-dir -r requirements.txt
ADD --chown=app:app . .

CMD env/bin/python manage.py migrate && env/bin/python manage.py collectstatic --no-input && env/bin/gunicorn --workers $GUNICORN_WORKERS --threads $GUNICORN_THREADS --bind :$PORT --timeout $GUNICORN_TIMEOUT $GUNICORN_APP_MODULE

