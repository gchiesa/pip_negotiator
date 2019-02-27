#!/usr/bin/env python
import os
import shlex
import subprocess
import tempfile
from subprocess import CalledProcessError

from .base import ShellCommand

__author__ = "Giuseppe Chiesa"
__copyright__ = "Copyright 2017, Giuseppe Chiesa"
__credits__ = ["Giuseppe Chiesa"]
__license__ = "BSD"
__maintainer__ = "Giuseppe Chiesa"
__email__ = "mail@giuseppechiesa.it"
__status__ = "PerpetualBeta"


class PipCompileException(Exception):
    pass


class PipCompile(ShellCommand):
    COMMAND = 'pip-compile'
    ARGS = '--rebuild -U -v'

    def __init__(self, requirements):
        super(PipCompile, self).__init__()
        self._requirements = requirements
        self._tmp = tempfile.NamedTemporaryFile(delete=False)
        self._tmp.close()

    def execute(self):
        arguments = '{a} -o {o} {r}'.format(a=self.ARGS,
                                            o=self._tmp.name,
                                            r=self._requirements)
        try:
            result = subprocess.check_output(shlex.split('{c} {a}'.format(c=self.COMMAND, a=arguments)))
            self.logger.debug('Result from command {c} with args {a}: \n---{r}\n---\n'.format(c=self.COMMAND,
                                                                                              a=arguments, r=result))
        except CalledProcessError as e:
            self.logger.error('Error while calling: {p}'.format(p=e.cmd))
            raise PipCompileException(e.output)
        self._result = result
        return self

    @property
    def result(self):
        with open(self._tmp.name, 'rb') as fh:
            data = fh.readlines()
        return '\n'.join([line.strip() for line in data if not line.startswith('#')])
