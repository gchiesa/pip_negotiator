#!/usr/bin/env python
import abc
import logging
import logging.config

from .. import __application__

__author__ = "Giuseppe Chiesa"
__copyright__ = "Copyright 2017, Giuseppe Chiesa"
__credits__ = ["Giuseppe Chiesa"]
__license__ = "BSD"
__maintainer__ = "Giuseppe Chiesa"
__email__ = "mail@giuseppechiesa.it"
__status__ = "PerpetualBeta"


class ShellCommand:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.logger = logging.getLogger('{a}.{c}'.format(a=__application__, c=self.__class__.__name__))
        self._result = None
        super(ShellCommand, self).__init__()

    @abc.abstractmethod
    def execute(self):
        raise RuntimeError('Not Implemented')

    @property
    @abc.abstractmethod
    def result(self):
        raise RuntimeError('Not Implemented')
