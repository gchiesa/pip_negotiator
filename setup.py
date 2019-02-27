#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Giuseppe Chiesa",
    author_email='mail@giuseppechiesa.it',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    description="A simple tool with the goal to  keep your pip packages without conflicts",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pip_negotiator',
    name='pip_negotiator',
    packages=find_packages(include=['pip_negotiator']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/gchiesa/pip_negotiator',
    version='1.2.0',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pip-negotiator = pip_negotiator.pip_negotiator:main',
            'pip_negotiator = pip_negotiator.pip_negotiator:main',
        ]
    }
)
