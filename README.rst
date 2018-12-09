==============
Pip Negotiator
==============


.. image:: https://img.shields.io/pypi/v/pip_negotiator.svg
        :target: https://pypi.python.org/pypi/pip_negotiator

.. image:: https://img.shields.io/travis/gchiesa/pip_negotiator.svg
        :target: https://travis-ci.org/gchiesa/pip_negotiator

.. image:: https://readthedocs.org/projects/pip-negotiator/badge/?version=latest
        :target: https://pip-negotiator.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




A simple tool with the goal to  keep your pip packages without conflicts


* Free software: BSD license
* Documentation: https://pip-negotiator.readthedocs.io.


Features
--------

Pip Negotiator, read your requirements.txt file and create a new set of pinned requirements without conflicts with the
already existing packages.

Usage::

    pip-negotiator requirements.txt

Help::

    pip-negotiator --help




Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
