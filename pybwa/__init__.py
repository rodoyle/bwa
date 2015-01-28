#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import logging

from pyramid.paster import get_appsettings
from sqlalchemy.engine import engine_from_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


__author__ = "rodoyle"
__copyright__ = "Copyright 2014, Desktop Genetics Ltd"
__credits__ = ["rodoyle"]
__license__ = "Proprietary"
__version__ = "0.0.1"
__maintainer__ = "Riley Doyle"
__email__ = "rileyd@desktopgenetics.com"
__status__ = "Development"

log = logging.getLogger(__name__)


class Thing(object):
    """

    """
    pass  # much code deleted


def main(args, session):
    """

    """
    pass


if __name__ == '__main__':  # code to execute if called from command-line
    import argparse

    parser = argparse.ArgumentParser(description='Bulk loader')
    parser.add_argument('configfile', help='Configuration file')
    parser.add_argument('batch_id', help='batch_id to restart')
    args = parser.parse_args()
    settings = get_appsettings(args.configfile)
    engine = engine_from_config(settings, 'sqlalchemy.')
    # Shut up SQLAlchemy
    logging.basicConfig()
    log.setLevel(logging.DEBUG)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARN)
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    main(args, session)