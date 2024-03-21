from datetime import datetime

from pydantic import BaseModel

from .route import Route

__all__ = ["Report"]


class Report(BaseModel):
    routes: list[Route]
    created_at: datetime
