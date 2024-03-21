from datetime import datetime, time

from selectolax.parser import HTMLParser

from ..models import Report, Route, Station
from ..settings import logger


def parse_html(html: str) -> Report:
    tree = HTMLParser(html)
    section = tree.css_first("#main-wrapper div.section.group")
    report = Report(
        routes=parse_section(section),
        created_at=datetime.now(),
    )
    logger.info(f"Parsed {len(report.routes)} routes")
    return report


def parse_section(section) -> list[Route]:
    # section.unwrap_tags(["p"])
    routes = []
    for h2 in section.css("h2"):
        route_name = h2.text(strip=True)
        logger.info(f"Parsing route {route_name}")
        stations = []
        current_node = h2.next
        while current_node:
            if current_node.tag == "h2":
                break
            if current_node.tag == "details":
                station = parse_details(current_node)
                stations.append(station)
            current_node = current_node.next
        routes.append(Route(name=route_name, stations=stations))
    return routes


def parse_details(details) -> Station:
    summary = details.css_first("summary")
    station_name = summary.css_first("strong").text()
    logger.debug(f"\tParsing station {station_name!r}")
    em = summary.css_first("em")
    station_direction = em.text() if em else None
    workdays, holidays = map(parse_li, details.css("li"))
    return Station(
        name=station_name,
        direction=station_direction,
        workdays_departure=workdays,
        holidays_departure=holidays,
    )


def parse_li(li) -> list[time | str]:
    text = li.text(strip=True)
    _, schedule_text = text.split(":", 1)
    schedule = []
    for time_text in schedule_text.split("-"):
        time_text = time_text.strip()
        try:
            time = datetime.strptime(time_text, "%H:%M").time()
        except ValueError:
            time = f"!!! {time_text}"
            logger.error(f"wrong time format: {time_text!r}")
        schedule.append(time)
    return schedule
