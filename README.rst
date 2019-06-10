**********************************
Pig Latin Translater Microservice
**********************************

Setup
=====

No local setup should be needed apart from:

- `docker <https://docs.docker.com/engine/installation/>`__
- `docker-compose <https://docs.docker.com/compose/>`__

Build the app
-------------

Run in project directory:

.. code:: bash

    docker-compose build

Run the server
--------------

Run in project directory:

.. code:: bash

    docker-compose up


This will build the container based on the Dockerfile and docker-compose file
and start the local server at ``http://localhost:8080``

Using the application
=====================

there are many ways to use the application:

1. Goto your browser at ``http://localhost:8080`` type the text you want to be translated
into the input then click send and you'll get back a translated response below

2. open a terminal go to the project directory and type E.g ``python3 client.py 'Hello my name is Alice'``

Or you use ``curl`` E.g:
``curl -i -H "Content-Type: application/json" -X POST -d '{"word": "James"}'http://localhost:8080/api/v1/translate``

Run Unit Tests
--------------

There's few simple tests

You can run the tests two ways

1. in the project directory type ``python3 tests.py``
2. in the project directory type ``./test tests
