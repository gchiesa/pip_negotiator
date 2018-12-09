#!/usr/bin/env python
import logging
import subprocess
import abc
from . import __application__

__author__ = "Giuseppe Chiesa"
__copyright__ = "Copyright 2017, Giuseppe Chiesa"
__credits__ = ["Giuseppe Chiesa"]
__license__ = "BSD"
__maintainer__ = "Giuseppe Chiesa"
__email__ = "mail@giuseppechiesa.it"
__status__ = "PerpetualBeta"


class ShellCommand(object):
    def __init__(self):
        self.logger = logging.getLogger('{a}.{c}'.format(a=__application__, c=self.__class__.__name__))



class PipInventory(object):
    pass


class PipCompile(object):
    pass


def create_inventory_base():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
