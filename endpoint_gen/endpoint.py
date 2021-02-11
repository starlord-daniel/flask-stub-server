import json

from flask import Flask, Response

from .endpoint_config import EndpointConfig


def configure_endpoints(app: Flask, config_path: str) -> list[str]:
    ''' Configure endpoints based on the JSON config file

    Parameters
    ----------
    app: Flask
        The application that runs the Flask server

    config_path : str
        Path to the config JSON file to create the endpoints.

        Example:

        {
            "endpoints": [
                {
                    "name": "hello",
                    "methods": ["GET"],
                    "route": "/",
                    "headers": {},
                    "file_path": ""
                }
            ]
        }

    Returns
    -------
    list[str]
        A list of configured endpoints

    '''
    created_endpoints = []

    # get the file contents
    config_text = __read_file(config_path)
    try:
        # convert from json to dict
        config_dict = json.loads(config_text)
        config_dict = list[EndpointConfig](config_dict["endpoints"])

        # Create Endpoint loop: for each endpoint in config:
        for endpoint in config_dict:
            # Create single endpoint from config
            __create_endpoint(app, endpoint)

            # Add endpoint to list of created endpoints
            created_endpoints.append(endpoint["route"])

            return created_endpoints
    except Exception as e:
        raise TypeError(f"Supplied config is invalid: {config_text}", e)


def __create_endpoint(app: Flask, endpoint_config: EndpointConfig):
    ''' Create a single endpoint from the given config

    Parameters
    ----------
    app: Flask
        The application that runs the Flask server

    endpoint_config : EndpointConfig
        The configuration of the endpoint, coming from a json file.
    '''
    def endpoint():
        response = Response(__read_file(endpoint_config["file_path"]))
        response.status_code = 200
        response.headers = endpoint_config["headers"]
        return response
    app.add_url_rule(
        rule=endpoint_config["route"],
        endpoint=endpoint_config["name"],
        view_func=endpoint,
        methods=endpoint_config["methods"])


# Helper function for reading file content
def __read_file(file_path: str) -> str:
    ''' Read the content of a file '''
    with open(file_path, "r") as file:
        text = file.read()
        return text
