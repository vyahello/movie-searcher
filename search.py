from lib import movie_api
from lib.static import Endpoint


def _search_movies(endpoint: Endpoint) -> None:
    movie_api.run(address=endpoint.address, port=endpoint.port, debug=endpoint.debug)


if __name__ == "__main__":
    _search_movies(Endpoint())
