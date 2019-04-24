Apfelschuss
===========

.. image:: https://travis-ci.org/Apfelschuss/apfelschuss.svg?branch=master
    :target: https://travis-ci.org/Apfelschuss/apfelschuss
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

All Swiss citizens who have reached the age of 18 are `entitled to vote`_ and participate in elections at federal level. Approximately four times a year, voting occurs over various issues.

Apfelschuss is a web application that wants support Swiss in their decision-making. Registered users indicate prior to the votes whether they will accept or decline the individual initiatives and referendums. Other users can follow these statements.

More about voting in Switzerland can be `read on Wikipedia`_. Deployed application of this project on `apfelschuss.herokuapp.com`_.

.. _entitled to vote: https://youtu.be/yltRgOFYD-w
.. _read on Wikipedia: https://en.wikipedia.org/wiki/Voting_in_Switzerland
.. _`apfelschuss.herokuapp.com`: https://apfelschuss.herokuapp.com/

Getting Up and Running locally
------------------------------

The steps below will get you up and running with a local development environment. All of these commands assume you are in the root of your generated project.

Prerequisites
^^^^^^^^^^^^^

* Docker; if you don't have it yet, follow the `installation instructions`_;
* Docker Compose; refer to the official documentation for the `installation guide`_.
* `Node.js`_ JavaScript runtime for generating the frontend assets.

.. _`installation instructions`: https://docs.docker.com/install/#supported-platforms
.. _`installation guide`: https://docs.docker.com/compose/install/
.. _`Node.js`: https://nodejs.org/en/


Generating assets
^^^^^^^^^^^^^^^^^

1. Run in the root ``npm install``
2. Run ``npm run build``

For frontend development (sass, js and image generation on the fly) you can run ``npm run watch``. Assets are located in `apfelschuss/src`_ folder and will be moved to `apfelschuss/static`_. This project uses webpack_ as assets bundler.

.. _`apfelschuss/src`: https://github.com/Apfelschuss/apfelschuss/tree/master/apfelschuss/src
.. _`apfelschuss/static`: https://github.com/Apfelschuss/apfelschuss/tree/master/apfelschuss/static
.. _webpack : https://webpack.js.org


Running locally with Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This brings up both Django and PostgreSQL. The first time it is run it might take a while to get started, but subsequent runs will occur quickly.

Build the stack
~~~~~~~~~~~~~~~

Open a terminal at the project root and run the following for local development::

    $ docker-compose -f local.yml up

Run the stack
~~~~~~~~~~~~~

Open a terminal at the project root and run the following for local development::

    $ docker-compose -f local.yml up

Open a browser window and type ``http://127.0.0.1:8000``

Useful Django and Python commands
---------------------------------

As with any shell command that we wish to run in our container, this is done using the ``docker-compose -f local.yml run --rm`` command.

Make migrations and migrate database::

    $ docker-compose -f local.yml run --rm django python manage.py makemigrations
    $ docker-compose -f local.yml run --rm django python manage.py migrate

Creating a superuser::

    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

Testing with Pytest_::

    $ docker-compose -f local.yml run --rm django pytest

.. _Pytest: https://docs.pytest.org/en/latest/example/simple.html

Check test coverage, and generate an HTML coverage report::

    $ docker-compose -f local.yml run django coverage run -m pytest
    $ docker-compose -f local.yml run django coverage report

For unit tests, run::

    $ docker-compose -f local.yml run --rm django python manage.py test

Check linting with flake8::

    $ docker-compose -f local.yml run --rm django flake8

Running type checks with mypy::

    $ docker-compose -f local.yml run --rm django mypy apfelschuss


Internationalization and Localization
-------------------------------------

We aim to keep up translations of the four Swiss national languages. Default language is English:

* en-US (English)
* de-CH (German)
* fr-CH (French)
* it-CH (Italian)
* rm (Raeto-Romance)

Create message files for all languages (see \*.po files in `locale folder`_)::

    $ docker-compose -f local.yml run django python manage.py makemessages -l de_CH -l fr_CH -l it_CH -l rm

Compile messages for creating \*.mo files based on \*.po files with following command::

    $ docker-compose -f local.yml run --rm django python manage.py compilemessages

.. _`locale folder`: ./locale


Credits
-------

Many thanks to:

* The contributors_. Actually at the moment it is just one, but everyone is welcome.
* Django_ the web framework for perfectionists with deadlines.
* All package providers of this project (see `requirements folder`_).
* `Cookiecutter Django`_ is a framework for jumpstarting production-ready Django projects.
* `sentry.io`_ open source error tracking that helps developers monitor and fix crashes in real time.
* `pyup.io`_ Python dependency security that keeps your dependencies up-to-date and compliant.

.. _contributors: https://github.com/Apfelschuss/apfelschuss/graphs/contributors
.. _Django: https://www.djangoproject.com
.. _`requirements folder`: https://github.com/Apfelschuss/apfelschuss/tree/master/requirements
.. _`Cookiecutter Django`: https://github.com/pydanny/cookiecutter-django
.. _`sentry.io`: https://sentry.io
.. _`pyup.io`: https://pyup.io/

License
-------

Apfelschuss is published under the `GNU GPLv3`_ license. See `license file`_ for more details.

**TL;DR**: You may copy, distribute and modify the software as long as you track changes/dates in source files. Any modifications to or software including (via compiler) GPL-licensed code must also be made available under the GPL along with build & install instructions.

.. _`GNU GPLv3`: https://www.gnu.org/licenses/gpl-3.0.html
.. _`license file`: https://github.com/Apfelschuss/apfelschuss/blob/master/LICENSE
