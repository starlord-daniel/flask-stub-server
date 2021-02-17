from unittest import TestCase
from flask import Flask, Response
from src import configure_endpoints
from werkzeug.routing import Map

app = Flask(__name__)


class ResponseTests(TestCase):

    def test_endpoint_simple(self):
        with app.test_client() as test_client:
            configure_endpoints(app, "tests/functional/data/test_endpoint_simple_config.json")
            response: Response = test_client.get('/')
            assert response.status_code == 200
            assert response.content_type == "text/plain"
            assert b"Hello simple test. I hope you are doing well." in response.data
        # Reset the apps url_map after testing (or else we get duplicate routes)
        app.url_map = Map()

    def test_multiple_inline_endpoints(self):
        with app.test_client() as test_client:
            configure_endpoints(
                app, "tests/functional/data/test_multiple_simple_inline_endpoints.json")
            # Call to endpoint at "/"
            response: Response = test_client.get('/')
            assert response.status_code == 200
            assert response.content_type == "text/plain"
            assert b"Just a simple test, move along." in response.data

            # Call to endpoint at "/info"
            response: Response = test_client.get('/info')
            assert response.status_code == 200
            assert response.content_type == "text/plain"
            assert b"This is not the information you are looking for." in response.data
        # Reset the app after testing
        app.url_map = Map()
