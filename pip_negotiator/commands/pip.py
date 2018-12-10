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
        self._result = []
        try:
            for req_type in ['-o', '-u']:
                arguments = '{a} {t}'.format(a=self.ARGS, t=req_type)
                result = subprocess.check_output(shlex.split('{c} {a}'.format(c=self.COMMAND, a=arguments)),
                                                 stderr=devnull)
                self.logger.debug('Result from command {c} with args {a}: {r}'.format(c=self.COMMAND,
                                                                                      a=arguments, r=result))
                self._result.extend(self._parse_json(result))
        except CalledProcessError as e:
            self.logger.error('Error while calling: {p}'.format(p=e.cmd))
            raise
        finally:
            devnull.close()

        return self

    @staticmethod
    def _parse_json(data):
        try:
            result = json.loads(data)
        except TypeError as e:
            raise
        return result

    @property
    def result(self):
        if not self._result:
            self.execute()
        return self._result

    @property
    def inventory(self):
        self.logger.debug('Using exclusions: {}'.format(self._exclusions))
        return [elem['name'] for elem in self.result if elem['name'].lower() not in self._exclusions]

    def to_requirements(self):
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tmp.write('\n'.join(self.inventory))
        tmp.close()
        return Requirements([tmp.name])
