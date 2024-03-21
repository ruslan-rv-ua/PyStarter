from datetime import time

from pydantic import BaseModel

__all__ = ["Station"]


class Station(BaseModel):
    name: str
    direction: str | None
    workdays_departure: list[time | str]
    holidays_departure: list[time | str]
