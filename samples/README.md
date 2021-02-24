# Samples

The samples contained in this folder give an overview of the capabilities and usage of the package.

It is necessary to install the published packages before running the samples.

## Simple

This sample creates to endpoints: "/" and "/info". The "/" endpoint returns the text from the [hello.txt](simple/data/hello.txt) file and the other one exports data written directly inside the JSON config file [endpoints.json](simple/config/endpoints.json).

To start the server, use the Dockerfile. Change your directory to samples/simple and execute the following commands, after updating IMAGE and TAG:

```bash
docker build -t IMAGE:TAG .
docker run --rm -p 5000:5000 IMAGE:TAG
```
