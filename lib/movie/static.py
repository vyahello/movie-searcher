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
        return str(self.value)


@dataclass(frozen=True)
class Route:
    """The class represents API routes."""

    home: str = "/"
    search_single_keyword: str = "/api/search/{keyword}"
    single_director: str = "/api/director/{director_name}"
    top_ten: str = "/api/movie/top"
    all_genres: str = "/api/movie/genre/all"
    single_genre: str = "/api/movie/genre/{genre}"
    single_imdb_movie: str = "/api/movie/{imdb_number}"
