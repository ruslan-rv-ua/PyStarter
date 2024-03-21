import sys

from loguru import logger

URL = "https://mpmr.gov.ua/miski-avtobusni-marsruti.html"

logger.remove()
logger.add(
    sys.stderr,
    format="{level} {message}",
    level="INFO",
)
logger.add(
    "bus_schedule.log",
    format="{level} {message}",
    level="DEBUG",
    mode="w",
)
