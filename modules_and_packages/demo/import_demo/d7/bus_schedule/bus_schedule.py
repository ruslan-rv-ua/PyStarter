from pathlib import Path

from .grabber import get_bus_schedule_html
from .models import Report
from .parser import parse_html

__all__ = ["get_report"]


def get_report() -> Report:
    report = parse_html(get_bus_schedule_html())
    return report


def save_report(report: Report, file_path: Path | str = "report.json") -> None:
    file_path = Path(file_path)
    json_dump = report.model_dump_json(indent=4)
    Path(file_path).write_text(json_dump, encoding="utf-8")
