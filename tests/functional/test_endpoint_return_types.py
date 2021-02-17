from unittest import TestCase
from flask import Flask, Response
from src import configure_endpoints
from werkzeug.routing import Map

app = Flask(__name__)


class ReturnTypeTest(TestCase):

    def test_json_response(self):
        with app.test_client() as test_client:
            configure_endpoints(
                app, "tests/functional/data/test_json_response_config.json")
            response: Response = test_client.get('/json')
            assert response.status_code == 200
            assert response.content_type == "application/json"
            assert response.json["message"] == "Part of the call is the response."
        # Reset the apps url_map after testing (or else we get duplicate routes)
        app.url_map = Map()
