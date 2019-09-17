from responder import Request, Response
from lib import movie_api


@movie_api.route("/")
def index(_: Request, response: Response) -> None:
    response.content = movie_api.template("home/index.html")
