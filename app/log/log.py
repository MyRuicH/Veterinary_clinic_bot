import logging
import sys


logging.basicConfig(level=logging.INFO, stream=sys.stdout)


def get_log(msg: str) -> None:
    logging.log(level=logging.INFO, msg=msg)