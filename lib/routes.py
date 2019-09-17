from responder import Request, Response
from lib import movie_api
from lib.data.database import movie_to_dict, find_by_imdb, global_init, search_keyword, search_director
from lib.logging import MainLogger
from lib.static import ResponseCount

_logger = MainLogger(__name__)

global_init()


@movie_api.route("/")
def index(_: Request, response: Response) -> None:
    response.content = movie_api.template("home/index.html")


@movie_api.route("/api/search/{keyword}")
def search_by_keyword(_: Request, response: Response, keyword: str) -> None:
    movies = search_keyword(keyword)
    _logger.info("Searching for movie by keyword: %s", keyword)
    limited: bool = len(movies) > ResponseCount.MAX.value
    if len(movies) > ResponseCount.MAX.value:
        movies = movies[:10]

    movie_dicts = [movie_to_dict(movie) for movie in movies]
    response.media = {"keyword": keyword, "hits": movie_dicts, "truncated_results": limited}


@movie_api.route("/api/director/{director_name}")
def search_by_director(_: Request, response: Response, director_name: str) -> None:
    movies = search_director(director_name)
    print("Searching for movie by director: %s", director_name)
    limited: bool = len(movies) > ResponseCount.MAX.value
    if len(movies) > ResponseCount.MAX.value:
        movies = movies[:10]

    movie_dicts = [movie_to_dict(movie) for movie in movies]

    response.media = {"keyword": director_name, "hits": movie_dicts, "truncated_results": limited}


@movie_api.route("/api/movie/{imdb_number}")
def search_movie_by_imdb(_: Request, response: Response, imdb_number: str) -> None:
    response.media = movie_to_dict(find_by_imdb(imdb_number))


@movie_api.route("/api/movie/top")
def search_movie_top_ten(_: Request, response: Response) -> None:
    response.media = {"searching": "top"}


@movie_api.route("/api/movie/genre/all")
def search_all_genres(_: Request, response: Response) -> None:
    response.media = {"searching": "all genres"}
