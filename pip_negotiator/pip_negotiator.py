#!/usr/bin/env python
import argparse
import logging
import logging.config
import sys

from . import __application__, __version__
from .commands import PipCompile, PipInventory
from .commands.pipcompile import PipCompileException
from .requirements import Requirements

__author__ = "Giuseppe Chiesa"
__copyright__ = "Copyright 2017, Giuseppe Chiesa"
__credits__ = ["Giuseppe Chiesa"]
__license__ = "BSD"
__maintainer__ = "Giuseppe Chiesa"
__email__ = "mail@giuseppechiesa.it"
__status__ = "PerpetualBeta"


def configure_logging(level):
    """
    Configure the logging level of the tool
    :param level: level to set
    :return:
    """
    dconfig = {
        'version': 1,
        'formatters': {
            'simple': {
                'format': '[%(name)s] [%(levelname)s] : %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': level.upper(),
                'formatter': 'simple',
                'stream': 'ext://sys.stdout'
            }
        },
        'loggers': {
            __application__: {
                'level': level.upper(),
                'handlers': ['console'],
                'propagate': False
            },
            'pip._vendor.cachecontrol.controller': {
                'level': level.upper(),
                'handlers': ['console'],
                'propagate': False
            },
        },
        'root': {
            'level': level.upper(),
            'handlers': ['console']
        }
    }
    logging.config.dictConfig(dconfig)


def check_args():
    parser = argparse.ArgumentParser(prog=__application__)
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(__version__))
    parser.add_argument('-L', '--log-level', dest='log_level', required=False,
                        help='Log level to set',
                        choices=['debug', 'info', 'warning', 'error'],
                        default='info')
    parser.add_argument('-o', '--output',
                        help='Output file',
                        dest='output_file',
                        default=None)
    parser.add_argument('-e', '--exclusions',
                        help='Comma separated list of exclusions',
                        dest='exclusions',
                        default='')
    parser.add_argument('requirements', nargs='+',
                        help='Requirement files to process')
    return parser.parse_args()


def main():
    args = check_args()
    configure_logging(args.log_level)

    pip_inventory = PipInventory(args.exclusions.split(','))
    pip_inventory.execute()

    curr_requirements = pip_inventory.to_requirements()
    new_requirements = Requirements(args.requirements)

    total_requirements = Requirements([curr_requirements.to_catalog(), new_requirements.to_catalog()])

    try:
        pip_compile = PipCompile(total_requirements.to_catalog())
        pip_compile.execute()
    except PipCompileException as e:
        sys.stderr.write(e.message)
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(e.message)
        sys.exit(2)

    if args.output_file:
        with open(args.output_file, 'wb') as fh:
            fh.write(pip_compile.result)
    else:
        sys.stdout.write(pip_compile.result)


if __name__ == '__main__':
    main()
