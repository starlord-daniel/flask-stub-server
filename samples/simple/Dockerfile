FROM python:3.9-alpine

ENV FLASK_APP=simple.py

COPY . /flask-app

WORKDIR /flask-app

RUN python -m pip install --upgrade flask-stub-server

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]
