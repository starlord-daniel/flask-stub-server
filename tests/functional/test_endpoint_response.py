from unittest import TestCase
from flask import Flask, Response
from src import configure_endpoints

app = Flask(__name__)


class ResponseTests(TestCase):

    def test_endpoint_simple(self):
        with app.test_client() as test_client:
            configure_endpoints(app, "tests/functional/data/test_endpoint_simple_config.json")
            response: Response = test_client.get('/')
            assert response.status_code == 200
            assert response.content_type == "text/plain"
            assert b"Hello simple test. I hope you are doing well." in response.data
