#!/usr/bin/env python3.4

"""A simple web crawler -- main driver program."""

# TODO:
# - Add arguments to specify TLS settings (e.g. cert/key files).

import argparse
import logging
import sys

ARGS = argparse.ArgumentParser(description="Python CLI Utility")
ARGS.add_argument(
    '--iocp', action='store_true', dest='iocp',
    default=False, help='Use IOCP event loop (Windows only)')
ARGS.add_argument(
    '--select', action='store_true', dest='select',
    default=False, help='Use Select event loop instead of default')
ARGS.add_argument(
    'roots', nargs='*',
    default=[], help='Root URL (may be repeated)')
ARGS.add_argument(
    '--max_redirect', action='store', type=int, metavar='N',
    default=10, help='Limit redirection chains (for 301, 302 etc.)')
ARGS.add_argument(
    '--max_tries', action='store', type=int, metavar='N',
    default=4, help='Limit retries on network errors')
ARGS.add_argument(
    '--max_tasks', action='store', type=int, metavar='N',
    default=100, help='Limit concurrent connections')
ARGS.add_argument(
    '--exclude', action='store', metavar='REGEX',
    help='Exclude matching URLs')
ARGS.add_argument(
    '--strict', action='store_true',
    default=True, help='Strict host matching (default)')
ARGS.add_argument(
    '--lenient', action='store_false', dest='strict',
    default=False, help='Lenient host matching')
ARGS.add_argument(
    '-v', '--verbose', action='count', dest='level',
    default=2, help='Verbose logging (repeat for more verbose)')
ARGS.add_argument(
    '-q', '--quiet', action='store_const', const=0, dest='level',
    default=2, help='Only log errors')


def main():
    """Main program

    Parse arguments, set up event loop, run crawler, print report.
    """
    args = ARGS.parse_args()
    if not args.roots:
        print('Use --help for command line help')
        return

    levels = [logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG]
    logging.basicConfig(level=levels[min(args.level, len(levels)-1)])

    # Manipulate arguments and instantiate business logic

    try:
        # Call business logic
        import sample
        sample.crap()
    except KeyboardInterrupt:
        sys.stderr.flush()
        print('\nInterrupted\n')
    finally:
        # Report results and tear down
        pass


if __name__ == '__main__':
    main()