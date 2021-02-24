from unittest import TestCase
from unittest.mock import MagicMock, patch

from flask_stub_server.endpoint_gen import (
    read_file, configure_endpoints, create_endpoint)


class EndpointTest(TestCase):
    @patch("flask_stub_server.endpoint_gen.endpoint.create_endpoint")
    @patch("flask.Flask")
    def test_configure_endpoints(self, mock_Flask: MagicMock,
                                 mock_create_endpoint: MagicMock):
        config_path = "tests/unit/data/test_configure_endpoints.json"
        configure_endpoints(app=mock_Flask, config_path=config_path)
        mock_create_endpoint.assert_called_once()

        config_path = "tests/unit/data/test_configure_endpoints_error.json"
        with self.assertRaises(Exception):
            configure_endpoints(mock_Flask, config_path)

    @patch("flask_stub_server.endpoint_gen.endpoint_config.EndpointConfig")
    @patch("flask.Flask.add_url_rule")
    @patch("flask.Flask")
    def test_create_endpoint(self, mock_app: MagicMock,
                             mock_add_url_rule: MagicMock,
                             mock_endpoint_config: MagicMock):
        exp_file_path = "path/file.json"
        exp_header = {}
        exp_route = "/"
        exp_name = "test"
        exp_methods = ["GET"]

        mock_endpoint_config.return_value = {
            "file_path": exp_file_path,
            "headers": exp_header,
            "route": exp_route,
            "name": exp_name,
            "methods": exp_methods
        }

        create_endpoint(app=mock_app, endpoint_config=mock_endpoint_config)

        mock_add_url_rule.assert_called_once()

    def test_read_file(self):
        file_path = "tests/unit/data/test_file.txt"
        expected_content = (b"This is a test\n"
                            b"it has multiple lines\n"
                            b"oh, even a third, that's crazy! :-O\n")

        actual_content = read_file(file_path=file_path)

        assert expected_content == actual_content
