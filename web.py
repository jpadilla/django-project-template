#!/usr/bin/env python
import logging
import os

import bjoern
from ipaddress import ip_address

from {{ project_name }}.wsgi import application

DEFAULT_HOST = os.environ.get('BIND_ADDR', '127.0.0.1')
DEFAULT_PORT = os.environ.get('BIND_PORT', 8002)

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    import argparse  # for parsing passed parameters through terminal

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-ip', help='Hostname', default='%s:%d' % (DEFAULT_HOST, DEFAULT_PORT),
        nargs='?',
    )  # either define an IP
    parser.add_argument('-socket', help='Linux Socket Name', default=None, nargs='?')  # or pass path of Linux's socket
    args = parser.parse_args()

    if args.socket:  # a socket is passed
        bjoern.run(application, 'unix:' + args.socket)
    else:
        if ':' in args.ip:
            ip, separator, port = args.ip.rpartition(':')
            ip = ip_address(ip.strip('[]'))
            port = int(port)
        else:
            ip = ip_address(args.ip.strip('[]'))
            port = DEFAULT_PORT

        ip = str(ip)
        try:
            logger.info('Starting web server. host=%s, port=%s' % (ip, port))
            bjoern.run(application, ip, port)
        except KeyboardInterrupt:
            logger.info('Shutting down web server.')
