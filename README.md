# Bloker

A Flask webapp to experiment with using Docker and Docker Compose for setting up a test environment.

## Images

We use prebuilt images from [Docker Hub](https://hub.docker.com/) to setup a test environment:

* `python:2.7` for running the web application and tests.
* `postgres` for the Database.


## Running tests

    sh scripts/run_tests.sh
