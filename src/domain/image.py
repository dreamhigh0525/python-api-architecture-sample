
from dataclasses import dataclass


@dataclass(frozen=True)
class Image:
    id: str
    data: str
