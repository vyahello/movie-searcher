[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/pylint-checked-blue)](https://www.pylint.org)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Build Status](https://travis-ci.org/vyahello/movie-search-api.svg?branch=master)](https://travis-ci.org/vyahello/movie-search-api)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/movie-search-api/badge.svg?branch=master)](https://coveralls.io/github/vyahello/movie-search-api?branch=master)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Hits-of-Code](https://hitsofcode.com/github/vyahello/movie-search-api)](https://hitsofcode.com/view/github/vyahello/movie-search-api)

# Movie searcher
> A lightweight movie search service written in [responder](http://python-responder.org/en/latest/) python HTTP service framework. 
> Please follow https://movie-search-rest-api.herokuapp.com link app to see how it looks like.

## Tools/features

### Production
- python 3.7
- responder framework
- vue js framework
- nginx
- docker 
- heroku deployment

### Development
- pytest framework
- travis & github CI

## Usage

### Frontend

![Screenshot](static/screen/web.png)

> The page could be accessed via `http://0.0.0.0:7777/index.html` endpoint.

### Backend (API docs)

![Screenshot](static/screen/api.png)

> The page could be accessed via `http://0.0.0.0:7777/api` endpoint.

#### Docker

Docker setup is based on docker-compose which consists of 3 official docker images:
- vyahello/movie-searcher-base
- vyahello/movie-searcher-backend  
- vyahello/movie-searcher-frontend

Please run the following command to launch an application via docker-compose (it uses [docker-compose.yml](docker-compose.yml) file):
```docker
cd docker && docker-compose up
```

#### Source code

Please run next commands to start an app via source code:
```bash
git clone git@github.com:vyahello/movie-search-api.git
pip install -r requirements.txt
python movie_searcher.py
```

## Development notes

### Code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy`, and `unittests` accordingly.
To be able to start static code analysis _locally_ please run following script from the root directory of the project:
```bash
./run-code-analysis.sh install-dependencies
```

### Deployment
Please refer to [deployment](DEPLOYMENT.md) page to get instructions on how to provision an app.

### Release notes
Please refer to [changelog](CHANGELOG.md) page for app release notes.

## Meta
Author – _Volodymyr Yahello_.

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (`git checkout -b feature/fooBar`)
6. Commit your changes (`git commit -am 'Add some fooBar'`)
7. Push to the branch (`git push origin feature/fooBar`)
8. Create a new Pull Request
