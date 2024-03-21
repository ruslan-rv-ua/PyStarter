from pydantic import BaseModel

from .station import Station

__all__ = ["Route"]


class Route(BaseModel):
    name: str
    stations: list[Station]
