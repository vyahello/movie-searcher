from lib.movie.static import HomeTemplate, Route
from lib.movie import movie_client
from responder import Request, Response

_route: Route = Route()
_home_template: HomeTemplate = HomeTemplate()


@movie_client.route(route=_route.home)
@movie_client.route(route=_route.index)
async def home(_: Request, response: Response) -> None:
    response.content = movie_client.template(_home_template.web)
