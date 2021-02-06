FROM python:3.9-alpine

ENV FLASK_APP=run.py

COPY . /flask-app

WORKDIR /flask-app

RUN python -m pip install -r dev-requirements.txt

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]
