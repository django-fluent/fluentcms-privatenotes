fluentcms-privatenotes
======================

.. image:: https://img.shields.io/travis/django-fluent/fluentcms-privatenotes/master.svg?branch=master
    :target: http://travis-ci.org/django-fluent/fluentcms-privatenotes
.. image:: https://img.shields.io/pypi/v/fluentcms-privatenotes.svg
    :target: https://pypi.python.org/pypi/fluentcms-privatenotes/
.. image:: https://img.shields.io/badge/wheel-yes-green.svg
    :target: https://pypi.python.org/pypi/fluentcms-privatenotes/
.. image:: https://img.shields.io/pypi/l/fluentcms-privatenotes.svg
    :target: https://pypi.python.org/pypi/fluentcms-privatenotes/
.. image:: https://img.shields.io/codecov/c/github/django-fluent/fluentcms-privatenotes/master.svg
    :target: https://codecov.io/github/django-fluent/fluentcms-privatenotes?branch=master

Adding Sticky-notes in the admin interface for content.

.. image:: https://raw.githubusercontent.com/django-fluent/fluentcms-privatenotes/master/docs/images/fluentcms-privatenotes.png
   :width: 954
   :height: 477


Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code-block:: bash

    pip install fluentcms-privatenotes

First make sure the project is configured for django-fluent-contents_.

Then add the following settings:

.. code-block:: python

    INSTALLED_APPS += (
        'fluentcms_privatenotes',
    )

    FLUENT_CONTENTS_PLACEHOLDER_CONFIG = {
        'slot name': {
            'plugins': ('PrivateNotesPlugin', ...),
        },
    }

The database tables can be created afterwards:

.. code-block:: bash

    ./manage.py migrate


Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

.. _django-fluent-contents: https://github.com/django-fluent/django-fluent-contents
