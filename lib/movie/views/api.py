from typing import List, Dict, Any
from responder import Request, Response
from lib.movie import movie_client
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
from lib.movie.static import HomeTemplate, ResponseCount, Route

_logger: Logger = MainLogger(__name__)
_route: Route = Route()
_home_template: HomeTemplate = HomeTemplate()


def _hits(movies: List[Movie]) -> List[Dict[Any, Any]]:
    if len(movies) > ResponseCount.MAX.value:
        movies = movies[: ResponseCount.MAX.value]

    return [movie_to_dict(movie) for movie in movies]


@movie_client.route(route=_route.api)
async def home(_: Request, response: Response) -> None:
    response.content = movie_client.template(_home_template.api)


@movie_client.route(route=_route.search_single_keyword)
async def search_by_keyword(
    _: Request, response: Response, keyword: str
) -> None:
    movies = search_keyword(keyword)
    _logger.info("Searching for movie by keyword: %s", keyword)
    limited: bool = len(movies) > ResponseCount.MAX.value
    response.media = {
        "keyword": keyword,
        "hits": _hits(movies),
        "truncated_results": limited,
    }


@movie_client.route(route=_route.single_director)
async def search_by_director(
    _: Request, response: Response, director_name: str
) -> None:
    movies = search_director(director_name)
    _logger.info("Searching for movie by director: %s", director_name)
    limited: bool = len(movies) > ResponseCount.MAX.value
    response.media = {
        "keyword": director_name,
        "hits": _hits(movies),
        "truncated_results": limited,
    }


@movie_client.route(route=_route.top_ten)
async def search_movie_top_ten(_: Request, response: Response) -> None:
    movies = movies_by_popularity()
    _logger.info("Searching for top 10 movies")
    limited: bool = len(movies) > ResponseCount.MAX.value
    response.media = {
        "keyword": f"top_{ResponseCount.MAX.value}",
        "hits": _hits(movies),
        "truncated_results": limited,
    }


@movie_client.route(route=_route.all_genres)
async def search_all_genres(_: Request, response: Response) -> None:
    response.media = all_genres()


@movie_client.route(route=_route.single_genre)
async def search_movies_by_genre(
    _: Request, response: Response, genre: str
) -> None:
    movies = movies_by_genre(genre)
    _logger.info(
        "Searching for movies by genre %s, %s results", genre, len(movies)
    )
    limited: bool = len(movies) > ResponseCount.MAX.value
    response.media = {
        "genre": genre,
        "hits": _hits(movies),
        "truncated_results": limited,
    }


@movie_client.route(route=_route.single_imdb_movie)
async def search_movie_by_imdb(
    _: Request, response: Response, imdb_number: str
) -> None:
    movie = find_by_imdb(imdb_number)
    _logger.info(
        "Looking up movie by code: %s, found? %s",
        imdb_number,
        "Yes" if movie else "NO",
    )
    response.media = movie_to_dict(movie)
