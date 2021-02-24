# Simple Flask Stub Server

[![Test package with tox](https://github.com/starlord-daniel/flask-stub-server/actions/workflows/ci-pr.yml/badge.svg?branch=main)](https://github.com/starlord-daniel/flask-stub-server/actions/workflows/ci-pr.yml)

Provides the user with a Docker container, that exposes endpoints, which can be configured via json file.

## Get Started with Flask

[Documentation on the Flask website](https://flask.palletsprojects.com/en/1.1.x/installation/)

## Configure your server

The file `endpoints.json` is used to configure the server endpoints.
To learn more about the format of the configuration file, please take a look at [Configuring the server endpoints](docs/configure-endpoints.md)

Also, the [samples directory](samples/README.md) shows examples on how to configure and quickly use your own endpoint server.

## Development

This project uses a virtual environment for development.

More information can be found on the [Flask installation website](https://flask.palletsprojects.com/en/1.1.x/installation/#virtual-environments).

## Testing

For testing, this project uses `tox`. The tox.ini configures 2 environments: lint and py39.

To only run linting, use: `tox -e lint`
To only run the tests with pytest, use: `tox -e py39`

## Package

View the package [flask-stub-server on pypi](https://pypi.org/project/flask-stub-server/)

The package can be installed by running:

```bash
pip install flask-stub-server
```

To upgrade the package, use:

```bash
pip install --upgrade flask-stub-server
```
