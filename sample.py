import logging

LOGGER = logging.getLogger(__name__)

def crap():
    LOGGER.info(f'{__name__} "INFO"')
    LOGGER.warn(f'{__name__} "WARN"')