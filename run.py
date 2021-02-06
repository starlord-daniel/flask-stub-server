# Flask docu: https://flask.palletsprojects.com/en/1.1.x/quickstart/
from flask import Flask
app = Flask(__name__)


# URL Route Registrations: https://flask.palletsprojects.com/en/1.1.x/api/#url-route-registrations
@app.route('/')
def hello_world():
    return 'Hello, World!'
