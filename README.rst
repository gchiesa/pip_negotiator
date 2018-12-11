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

This is useful when you want to install new Python Packages in a system without introducing conflicts.

All the packages dependencies will be resolved by including the list of the already installed Python Packages. The result
is a new output (requirements.txt format) that can be used with pip


Usage::

    pip-negotiator -o resolved_requirements.txt requirements.txt
    pip install -U resolved_requirements.txt

In case there is an error and the requirements cannot be resolved, use the debug mode to get an extensive analysis::

    pip-negotiator -L debug requirements.txt


Help::

    pip-negotiator --help



Credits
-------

Pip Negotiator it's a wrapper around pip_ and pip-tools_
This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _pip: https://pypi.org/project/pip/
.. _pip-tools: https://pypi.org/project/pip-tools/

