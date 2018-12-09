#!/usr/bin/env python
import json
import os
import shlex
import subprocess
import tempfile
from subprocess import CalledProcessError

from .base import ShellCommand
from ..requirements import Requirements

__author__ = "Giuseppe Chiesa"
__copyright__ = "Copyright 2017, Giuseppe Chiesa"
__credits__ = ["Giuseppe Chiesa"]
__license__ = "BSD"
__maintainer__ = "Giuseppe Chiesa"
__email__ = "mail@giuseppechiesa.it"
__status__ = "PerpetualBeta"


class PipInventory(ShellCommand):
    COMMAND = 'pip'
    ARGS = 'list --format=json'

    def __init__(self, exclusions=None):
        super(PipInventory, self).__init__()
        self._data = None
        self._exclusions = []
        if exclusions:
            self._exclusions = [elem.lower().strip() for elem in exclusions]

    def execute(self):
        devnull = open(os.devnull, 'w')
        try:
            result = subprocess.check_output(shlex.split('{c} {a}'.format(c=self.COMMAND, a=self.ARGS)), stderr=devnull)
            self.logger.debug('Result from command {c} with args {a}: {r}'.format(c=self.COMMAND,
                                                                                  a=self.ARGS, r=result))
        except CalledProcessError as e:
            self.logger.error('Error while calling: {p}'.format(p=e.cmd))
            raise
        finally:
            devnull.close()
        self._result = result
        return self

    @property
    def result(self):
        if self._data:
            return self._data
        try:
            self._data = json.loads(self._result)
        except TypeError:
            self.logger.error('Result is not valid. Actual content: {}'.format(self._result))
            return None
        return self._data

    @property
    def inventory(self):
        self.logger.debug('Using exclusions: {}'.format(self._exclusions))
        return [elem['name'] for elem in self.result if elem['name'].lower() not in self._exclusions]

    def to_requirements(self):
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tmp.write('\n'.join(self.inventory))
        tmp.close()
        return Requirements([tmp.name])
