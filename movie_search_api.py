"""Module contains API to work with `movie-searcher` app."""
from abc import ABC, abstractmethod
from lib.movie import movie_api
from lib.movie.data.database import global_init
from lib.movie.static import Endpoint


class Service(ABC):
    """The class represents abstract interface for service."""

    @abstractmethod
    def start(self) -> None:
        """Starts abstract searcher."""
        pass


class MovieSearcher(Service):
    """The class represents movie searcher engine."""

    def __init__(self, endpoint: Endpoint) -> None:
        self._endpoint = endpoint

    def start(self) -> None:
        """Starts movie searcher."""
        global_init()
        movie_api.run(address=self._endpoint.address, port=self._endpoint.port, debug=self._endpoint.debug)


def main() -> None:
    """Runs an application."""
    searcher: Service = MovieSearcher(Endpoint())
    searcher.start()


if __name__ == "__main__":
    main()
