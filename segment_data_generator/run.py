from time import sleep
import analytics as segment
import faker as faker
import logging
import argparse
import sys
from segment_data_generator import __version__
from segment_data_generator import utils as utils
from random import randint


__author__ = "lilstipher"
__copyright__ = "lilstipher"
__license__ = "MIT"

_logger = logging.getLogger(__name__)
def parse_args(args):
    """Parse command line parameters
    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).
    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Segment Data generator")
    parser.add_argument(
        "--version",
        action="version",
        version="segment-data-generator {ver}".format(ver=__version__),
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    parser.add_argument(
        "-k",
        "--key",
        dest="write_key",
        type=str,
        required=True,
        help="put your segment write key",
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging
    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )





def gen_fake_data():
    ...

def main(args: list[str] ):
    """Wrapper
    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "confi.yaml"]``).
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.info(f"Log level set to {args.loglevel}")

    try :
        segment.write_key = args.write_key
        _logger.info("Write key set up")
    except Exception as err:
        _logger.error("Cannot setting the write key ! Exit...")
        exit(1)


    while True :
        uuid, traits = utils.generate_identify_data()
        event_id,event_name,event = utils.generate_track_data()
        rand = randint(0,1)
        if rand == 0 : 
            segment.identify(uuid, traits)
        else :
            segment.track(event_id,event_name,event)
        sleep(10)


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`
    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m segment_data_generator.run -vv
    #
    run()