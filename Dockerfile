FROM python:3.10-slim

RUN mkdir /05

WORKDIR /05

ADD . /05

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0:8000
