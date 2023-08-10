FROM python:3.10.10-alpine3.17

WORKDIR /app

COPY requirements.txt .

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "api.py"]