# Simple Flask Stub Server

[![Test package with tox](https://github.com/starlord-daniel/flask-stub-server/actions/workflows/ci-pr.yml/badge.svg?branch=main)](https://github.com/starlord-daniel/flask-stub-server/actions/workflows/ci-pr.yml)

Provides the user with a Docker container, that exposes endpoints, which can be configured via json file.

## Get Started with Flask

[Documentation on the Flask website](https://flask.palletsprojects.com/en/1.1.x/installation/)

## Configure your server

The file `endpoints.json` is used to configure the server endpoints.
To learn more about configuring the endpoints, please take a look at [Configuring the server endpoints](docs/configure-endpoints.md)

## Start the server

To start the server, use the docker container:

```bash
docker build -t IMAGE:TAG .
docker run -p 5000:5000 IMAGE:TAG
```

## Development

This project uses a virtual environment for development.

More information can be found on the [Flask installation website](https://flask.palletsprojects.com/en/1.1.x/installation/#virtual-environments).

## Testing

For testing, this project uses `tox`. The tox.ini configures 2 environments: lint and py39.

To only run linting, use: `tox -e lint`
To only run the tests with pytest, use: `tox -e py39`
