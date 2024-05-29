FROM python:3.10-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY pyproject.toml poetry.lock ./

# Install dependencies from poetry lock
RUN pip install --upgrade pip && \
    pip install poetry~=1.8.3 && \
    poetry export -f requirements.txt --output requirements.txt && \
    pip install -r requirements.txt

COPY ./app/ /usr/src/app/


