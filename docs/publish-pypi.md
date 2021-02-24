# Publish the package to PYPI

Take a look at the documentation about [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/) for a general overview.

Some things only have to happen once in your virutal environment:

- installing necessary tools to publish and build packages:

    ```bash
    pip install twine
    pip install setuptools
    pip install wheel
    ```

The specific steps that need to happen, every time a new package is created, are:

1. Update setup.py (mostly version changes) and other dependencies (requirements, Licence, etc.)
1. Run `python setup.py sdist bdist_wheel` to create **build** and **dist** directories
1. Run `twine check dist/*` to check the distribution for errors. The output should look similar to this:

    ```bash
    Checking dist/flask_stub_server-0.1.1.dev1-py3-none-any.whl: PASSED
    Checking dist/flask-stub-server-0.1.1.dev1.tar.gz: PASSED
    ```

1. Upload the package to your test pypi repo with `twine upload --repository testpypi dist/*`
1. Upload the package to your real pypi repo with `twine upload dist/*`
