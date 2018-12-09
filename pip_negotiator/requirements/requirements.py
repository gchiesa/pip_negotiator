#!/usr/bin/env python
import tempfile

__author__ = "Giuseppe Chiesa"
__copyright__ = "Copyright 2017, Giuseppe Chiesa"
__credits__ = ["Giuseppe Chiesa"]
__license__ = "BSD"
__maintainer__ = "Giuseppe Chiesa"
__email__ = "mail@giuseppechiesa.it"
__status__ = "PerpetualBeta"


class Requirements(object):
    def __init__(self, requirement_files):
        self._files = requirement_files
        self.file = None

    def to_catalog(self):
        self.file = tempfile.NamedTemporaryFile(delete=False)
        for f in self._files:
            with open(f, 'rb') as fh:
                data = fh.read().strip()
                self.file.write('{}\n'.format(data))
        self.file.close()
        return self.file.name
