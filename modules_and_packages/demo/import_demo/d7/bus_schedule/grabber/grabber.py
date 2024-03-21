import requests

from ..settings import URL, logger


def get_bus_schedule_html() -> str:
    logger.info("Fetching bus schedule from mpmr.gov.ua")
    r = requests.get(URL)
    return r.text
