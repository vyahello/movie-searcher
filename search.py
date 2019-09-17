from lib.movie import movie_api
from lib.movie.data.database import global_init
from lib.movie.static import Endpoint


class MovieSearcher:
    def __init__(self, endpoint: Endpoint) -> None:
        self._endpoint = endpoint

    def start(self) -> None:
        global_init()
        movie_api.run(address=self._endpoint.address, port=self._endpoint.port, debug=self._endpoint.debug)


if __name__ == "__main__":
    searcher: MovieSearcher = MovieSearcher(Endpoint())
    searcher.start()
