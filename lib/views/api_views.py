from responder import Request, Response
from lib import movie_api
from lib.data.database import (
    search_keyword,
    movie_to_dict,
    search_director,
    find_by_imdb,
    all_genres,
    movies_by_popularity,
)
from lib.logging import Logger, MainLogger
from lib.static import ResponseCount

_logger: Logger = MainLogger(__name__)


@movie_api.route("/api/search/{keyword}")
async def search_by_keyword(_: Request, response: Response, keyword: str) -> None:
    movies = search_keyword(keyword)
    _logger.info("Searching for movie by keyword: %s", keyword)
    limited: bool = len(movies) > ResponseCount.MAX.value
    if len(movies) > ResponseCount.MAX.value:
        movies = movies[:10]

    movie_dicts = [movie_to_dict(movie) for movie in movies]
    response.media = {"keyword": keyword, "hits": movie_dicts, "truncated_results": limited}


@movie_api.route("/api/director/{director_name}")
async def search_by_director(_: Request, response: Response, director_name: str) -> None:
    movies = search_director(director_name)
    _logger.info("Searching for movie by director: %s", director_name)
    limited: bool = len(movies) > ResponseCount.MAX.value
    if len(movies) > ResponseCount.MAX.value:
        movies = movies[:10]

    movie_dicts = [movie_to_dict(movie) for movie in movies]
    response.media = {"keyword": director_name, "hits": movie_dicts, "truncated_results": limited}


@movie_api.route("/api/movie/{imdb_number}")
async def search_movie_by_imdb(_: Request, response: Response, imdb_number: str) -> None:
    movie = find_by_imdb(imdb_number)
    _logger.info("Looking up movie by code: %s, found? %s".format(imdb_number, 'Yes' if movie else 'NO'))
    response.media = movie_to_dict(movie)


@movie_api.route("/api/movie/top")
async def search_movie_top_ten(_: Request, response: Response) -> None:
    hits = movies_by_popularity()
    _logger.info("Searching for top 10 movies")
    limited: bool = len(hits) > ResponseCount.MAX.value
    if limited:
        hits = hits[: ResponseCount.MAX.value]

    hits_dicts = [movie_to_dict(movie) for movie in hits]
    response.media = {"keyword": f"top_{ResponseCount.MAX.value}", "hits": hits_dicts, "truncated_results": limited}


@movie_api.route("/api/movie/genre/all")
async def search_all_genres(_: Request, response: Response) -> None:
    response.media = all_genres()
