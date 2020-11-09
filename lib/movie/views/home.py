from responder import Request, Response
from lib.movie import movie_api
from lib.movie.static import Route

_route: Route = Route()


@movie_api.route(route=_route.home)
async def index(_: Request, response: Response) -> None:
    response.content = movie_api.template("api/home/index.html")
