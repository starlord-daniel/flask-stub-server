import xml.etree.ElementTree as ET
from unittest import TestCase

from flask import Flask, Response
from werkzeug.routing import Map

from src import configure_endpoints

app = Flask(__name__)


class ReturnTypeTest(TestCase):

    def test_json_response(self):
        exp_json_message = "Part of the call is the response."
        with app.test_client() as test_client:
            configure_endpoints(
                app, "tests/functional/data/test_json_response_config.json")
            response: Response = test_client.get('/json')
            assert response.status_code == 200
            assert response.content_type == "application/json"
            assert response.json["message"] == exp_json_message
        # Reset the apps url_map after testing (or else we get duplicate routes)
        app.url_map = Map()

    def test_xml_response(self):
        exp_children = {
            "from": "Daniel",
            "content": "There should be less of this format and more proper JSON."
        }
        with app.test_client() as test_client:
            configure_endpoints(
                app, "tests/functional/data/test_xml_response_config.json")
            response: Response = test_client.get('/xml')
            # parse the xml from the returned string and point to its root element
            xml_root = ET.fromstring(response.get_data(as_text=True))
            assert response.status_code == 200
            assert response.content_type == "application/xml"
            assert xml_root.tag == "message"
            # Check the tags and value of the xml root child elements
            for child in xml_root:
                assert child.tag in exp_children.keys()
                assert child.text == exp_children[child.tag]

        # Reset the apps url_map after testing (or else we get duplicate routes)
        app.url_map = Map()
