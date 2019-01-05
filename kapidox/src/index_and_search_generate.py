#!/usr/bin/env python


# Python 2/3 compatibility (NB: we require at least 2.7)

import logging
import argparse
import sys
import os

from kapidox import generator, utils

DESCRIPTION = """\
"""

def main():

    utils.setup_logging()

    parser = argparse.ArgumentParser(description=DESCRIPTION)

    scriptdir = os.path.dirname(os.path.realpath(__file__))
    doxdatadir = os.path.join(scriptdir, 'kapidox/data')

    group = parser.add_argument_group('other arguments')

    group.add_argument('--doxdatadir', default=doxdatadir,
            help='Location of the HTML header files and support graphics.')

    group.add_argument('--title', default='API Documentation',
            help='String to use for page titles.')

    group.add_argument('--qhp', action='store_true',
            help='Generate Qt Compressed Help documentation.')

    group.add_argument('--configdir',
            help='Location of config files, metainfo.yaml, CMakeLists.txt and searchdata.json .')

    group.add_argument('--index-type', choices=['frameworks','apiref'],
            help='Type of the index page.', default= 'apiref')

    args = parser.parse_args()

    configdir = args.configdir
    doxdatadir = args.doxdatadir
    title = args.title
    qhp = args.qhp
    type = args.index_type
    if type == 'frameworks':
        logging.info('Generating docs for frameworks')
        generator.generate_index_frameworks(configdir, doxdatadir, title)
    else:
        generator.generate_index(configdir, doxdatadir, title, qhp)

    generator.generate_search(configdir)


if __name__ == "__main__":
    sys.exit(main())
