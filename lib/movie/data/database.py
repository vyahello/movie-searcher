import os
import csv
import collections
from dataclasses import dataclass
from typing import List, Dict, Any, Set, Optional

_movie_data: Dict[Any, Any] = dict()
_genres: Any = collections.defaultdict(list)
_top_movies: List[Any] = list()


@dataclass
class Movie:
    imdb_code: str
    director: str
    duration: int
    genres: Set[Any]
    title: str
    lower_title: int
    keywords: Set[Any]
    rating: Set[Any]
    year: float
    imdb_score: float


def movie_to_dict(movie: Movie) -> Dict[Any, Any]:
    if not movie:
        return {}

    data = dict(
        imdb_code=movie.imdb_code,
        title=movie.title,
        director=movie.director,
        keywords=list(movie.keywords),
        duration=movie.duration,
        genres=list(movie.genres),
        rating=movie.rating,
        year=movie.year,
        imdb_score=movie.imdb_score,
    )

    return data


def find_by_imdb(imdb_code: str) -> Any:
    global _movie_data
    movie = _movie_data.get(imdb_code)
    return movie


def search_keyword(keyword: str) -> List[Movie]:
    global _movie_data

    if not keyword:
        return []

    keyword = keyword.lower().strip()

    hits = []
    for movie in _movie_data.values():
        if movie.lower_title.find(keyword) >= 0:
            hits.append(movie)
        elif keyword in movie.keywords:
            hits.append(movie)

    return hits


def search_title(keyword: str) -> List[Movie]:
    global _movie_data

    if not keyword:
        return []

    return [
        movie
        for movie in _movie_data.values()
        if movie.lower_title.find(keyword.lower().strip()) >= 0
    ]


def search_director(director: str) -> List[Movie]:
    global _movie_data

    if not director:
        return []

    return [
        movie
        for movie in _movie_data.values()
        if movie.director.lower().find(director.lower().strip()) >= 0
    ]


def all_genres() -> List[str]:
    global _genres

    genre_names = [key for key in _genres]
    genre_names.sort(key=lambda number: number)

    return genre_names


def movies_by_genre(genre: str) -> List[Movie]:
    global _genres

    if not genre:
        return []

    genre = genre.lower().strip()
    return _genres.get(genre, [])


def movies_by_popularity() -> List[Movie]:
    return list(_top_movies)


def global_init() -> None:
    global _movie_data

    if _movie_data:
        return

    folder = os.path.dirname(__file__)
    file = os.path.join(folder, "movies.csv")

    with open(file, mode="r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)
        rows = list(reader)

    _movie_data = {}
    for row in rows:
        movie = Movie(  # type: ignore
            imdb_code=_build_imdb_code(
                row.get("movie_imdb_link", None)  # type: ignore
            ),
            director=row.get("director_name", "").strip(),
            rating=row.get("content_rating", "").strip(),
            title=row.get("movie_title", "").replace("\xa0", "").strip(),
            lower_title=row.get("movie_title", "")
            .replace("\xa0", "")
            .strip()
            .lower(),
            duration=_make_numerical(row.get("duration", 0)),  # type: ignore
            genres=set(  # type: ignore
                _split_separated_text(row.get("genres", "").lower())
            ),
            keywords=set(  # type: ignore
                _split_separated_text(row.get("plot_keywords", "").lower())
            ),
            imdb_score=float(row.get("imdb_score", 0.0)),
            year=_make_numerical(row.get("title_year", 0)),  # type: ignore
        )
        _movie_data[movie.imdb_code] = movie

    _build_genres()
    _build_top_movies()


def _build_top_movies() -> None:
    global _movie_data, _top_movies
    if _top_movies:
        return

    # Sort by score so top ranked movies appear first.
    _top_movies = list(_movie_data.values())
    _top_movies.sort(key=lambda movie: movie.imdb_score, reverse=True)


def _build_genres() -> None:
    global _movie_data, _genres
    if _genres:
        return

    for movie in _movie_data.values():
        for genre in movie.genres:
            _genres[genre.lower().strip()].append(movie)

    # Sort by score so we can easily get top 10 of any category.
    for _, movies in _genres.items():
        movies.sort(key=lambda movie_: movie_.imdb_score, reverse=True)


def _make_numerical(text: str) -> int:
    if not text or not text.strip():
        return 0

    return int(text)


def _build_imdb_code(link: str) -> Optional[str]:
    parts = link.split("/")
    if len(parts) < 5:
        return None

    return parts[4]


def _split_separated_text(text: str) -> Optional[Any]:
    if not text:
        return text

    return [
        part.strip()
        for part in text.strip().split("|")
        if part and part.strip()
    ]
