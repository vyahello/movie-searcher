from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Endpoint:
    """The class represents WEB endpoint for API."""

    address: str = "0.0.0.0"
    port: int = 7777
    debug: bool = False


class ResponseCount(Enum):
    """The class WEB response count item."""

    MAX: int = 10

    def __str__(self) -> str:
        return self.value
