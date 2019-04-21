Apfelschuss
===========

.. image:: https://travis-ci.org/Apfelschuss/apfelschuss.svg?branch=master
    :target: https://travis-ci.org/Apfelschuss/apfelschuss
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

All Swiss citizens who have reached the age of 18 are entitled to vote and participate in elections at federal level. Approximately four times a year, voting occurs over various issues.

Apfelschuss is a web application that wants support Swiss in their decision-making. Registered users indicate prior to the votes whether they will accept or decline the individual initiatives and referendums.
More about voting in Switzerland can be `read on Wikipedia`_.

.. _read on Wikipedia: https://en.wikipedia.org/wiki/Voting_in_Switzerland

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy apfelschuss

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html

Credits
-------

Many thanks to:

- the contributors_. Actually at the moment it is just one, but everyone is welcome.
- `Cookiecutter Django`_ is a framework for jumpstarting production-ready Django projects.
- `sentry.io`_ open source error tracking that helps developers monitor and fix crashes in real time.
- `pyup.io`_ Python dependency security that keeps your dependencies up-to-date and compliant.

.. _contributors: https://github.com/Apfelschuss/apfelschuss/graphs/contributors
.. _`Cookiecutter Django`: https://github.com/pydanny/cookiecutter-django
.. _`sentry.io`: https://sentry.io
.. _`pyup.io`: https://pyup.io/

License
-------

Apfelschuss is published under the `GNU GPLv3`_ license.

**TL;DR**: You may copy, distribute and modify the software as long as you track changes/dates in source files. Any modifications to or software including (via compiler) GPL-licensed code must also be made available under the GPL along with build & install instructions.

.. _`GNU GPLv3`: https://www.gnu.org/licenses/gpl-3.0.html
