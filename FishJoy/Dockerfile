FROM python:3.11.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

COPY ./requirements.txt /code/
RUN pip install -r /code/requirements.txt

COPY . /code/

EXPOSE 8000
