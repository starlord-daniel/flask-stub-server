import random

from tests.utils import get_random_string

from src.endpoint_gen import EndpointConfig


def test_endpoint_config_creation():
    name = get_random_string(12)
    route = '/'.join(
        [get_random_string(8), get_random_string(3)]
    )
    methods = random.choices(["GET", "POST", "DELETE", "PUT"], k=2)
    headers = {
        "Content-Type": "application/json",
        "Allow": "*"
    }
    file_path = f"data/{get_random_string(12)}.{get_random_string(3)}"

    config = EndpointConfig(name, route, methods, headers, file_path)

    assert config.name == name
    assert config.route == route
    assert config.methods == methods
    assert config.headers == headers
    assert config.file_path == file_path
