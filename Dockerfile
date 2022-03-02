FROM python:3.7

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /app
COPY . /app
WORKDIR /app
RUN chmod +x ./scripts/


CMD ["uwsgi","--http", "0.0.0.0:8000","--module", "auth.wsgi"]

