from typing import List, Dict, Any
from responder import Request, Response
from lib.movie import movie_api
from lib.movie.data.database import (
    Movie,
    search_keyword,
    movie_to_dict,
    search_director,
    find_by_imdb,
    all_genres,
    movies_by_popularity,
    movies_by_genre,
)
from lib.logging import Logger, MainLogger
from lib.movie.static import ResponseCount

_logger: Logger = MainLogger(__name__)


def _hits(movies: List[Movie]) -> List[Dict[Any, Any]]:
    if len(movies) > ResponseCount.MAX.value:
        movies = movies[: ResponseCount.MAX.value]

    return [movie_to_dict(movie) for movie in movies]


@movie_api.route("/api/search/{keyword}")
async def search_by_keyword(_: Request, response: Response, keyword: str) -> None:
    movies = search_keyword(keyword)
    _logger.info("Searching for movie by keyword: %s", keyword)
    limited: bool = len(movies) > ResponseCount.MAX.value
    response.media = {"keyword": keyword, "hits": _hits(movies), "truncated_results": limited}


@movie_api.route("/api/director/{director_name}")
async def search_by_director(_: Request, response: Response, director_name: str) -> None:
    movies = search_director(director_name)
    _logger.info("Searching for movie by director: %s", director_name)
    limited: bool = len(movies) > ResponseCount.MAX.value
    response.media = {"keyword": director_name, "hits": _hits(movies), "truncated_results": limited}


@movie_api.route("/api/movie/top")
async def search_movie_top_ten(_: Request, response: Response) -> None:
    movies = movies_by_popularity()
    _logger.info("Searching for top 10 movies")
    limited: bool = len(movies) > ResponseCount.MAX.value
    response.media = {"keyword": f"top_{ResponseCount.MAX.value}", "hits": _hits(movies), "truncated_results": limited}


@movie_api.route("/api/movie/genre/all")
async def search_all_genres(_: Request, response: Response) -> None:
    response.media = all_genres()


@movie_api.route("/api/movie/genre/{genre}")
async def search_movies_by_genre(_: Request, response: Response, genre: str):
    movies = movies_by_genre(genre)
    _logger.info("Searching for movies by genre %s, %s results", genre, len(movies))
    limited: bool = len(movies) > ResponseCount.MAX.value
    response.media = {"genre": genre, "hits": _hits(movies), "truncated_results": limited}


@movie_api.route("/api/movie/{imdb_number}")
async def search_movie_by_imdb(_: Request, response: Response, imdb_number: str) -> None:
    movie = find_by_imdb(imdb_number)
    _logger.info("Looking up movie by code: %s, found? %s", imdb_number, "Yes" if movie else "NO")
    response.media = movie_to_dict(movie)
