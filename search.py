from responder import API
from responder.models import Request, Response


if __name__ == "__main__":
    movie_api = API()

    @movie_api.route("/")
    def index(request: Request, response: Response) -> None:
        response.content = movie_api.template("home/index.html")

    movie_api.run(address="0.0.0.0", port=7777)
