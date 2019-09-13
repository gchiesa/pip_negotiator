#!/usr/bin/env python
import shlex
import subprocess
import tempfile
from subprocess import CalledProcessError

import six

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
    command = 'pip-compile'
    args = '--rebuild -U -v'

    def __init__(self, requirements):
        super(PipCompile, self).__init__()
        self._requirements = requirements
        self._tmp = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self._tmp.close()

    def execute(self):
        arguments = '{a} -o {o} {r}'.format(a=self.args,
                                            o=self._tmp.name,
                                            r=self._requirements)
        kwargs = {}
        if six.PY3:
            kwargs.update({'text': True})
        try:
            result = subprocess.check_output(shlex.split('{c} {a}'.format(c=self.resolve_command(), a=arguments)),
                                             **kwargs)
            self.logger.debug('Result from command {c} with args {a}: \n---{r}\n---\n'.format(c=self.resolve_command(),
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
        return '\n'.join([line.decode().strip() for line in data
                          if not line.decode().startswith('#')])
