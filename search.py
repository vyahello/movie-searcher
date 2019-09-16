from dataclasses import dataclass
from responder import API
from responder.models import Request, Response

movie_api = API()


@dataclass(frozen=True)
class Endpoint:
    """The class represents WEB endpoint for API."""

    address: str = "0.0.0.0"
    port: int = 7777


@movie_api.route("/")
def index(request: Request, response: Response) -> None:
    response.content = movie_api.template("home/index.html")


@movie_api.route("/api/search/{keyword}")
def search_by_keyword(request: Request, response: Response, keyword: str) -> None:
    response.media = {"searching": keyword}


@movie_api.route("/api/director/{director_name}")
def search_by_director(request: Request, response: Response, director_name: str) -> None:
    response.media = {"searching": director_name}


@movie_api.route("/api/movie/{imdb_number}")
def search_movie_by_imdb(request: Request, response: Response, imdb_number: str) -> None:
    response.media = {"searching": imdb_number}


@movie_api.route("/api/movie/top")
def search_movie_top_ten(request: Request, response: Response) -> None:
    response.media = {"searching": "top"}


@movie_api.route("/api/movie/genre/all")
def search_all_genres(request: Request, response: Response) -> None:
    response.media = {"searching": "all genres"}


@movie_api.route("/api/movie/genre/{genre}")
def search_all_genres(request: Request, response: Response, genre: str) -> None:
    response.media = {"searching": genre}


if __name__ == "__main__":
    endpoint = Endpoint()
    movie_api.run(address=endpoint.address, port=endpoint.port)
