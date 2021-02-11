# Flask docu: https://flask.palletsprojects.com/en/1.1.x/quickstart/
from flask import Flask
from endpoint_gen import configure_endpoints
app = Flask(__name__)


# URL Route Registrations: https://flask.palletsprojects.com/en/1.1.x/api/#url-route-registrations
endpoints = configure_endpoints(app, "config/endpoints.json")
print(endpoints)
