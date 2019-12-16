[![Build Status](https://travis-ci.org/vyahello/movie-search-api.svg?branch=master)](https://travis-ci.org/vyahello/movie-search-api)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/movie-search-api/badge.svg?branch=master)](https://coveralls.io/github/vyahello/movie-search-api?branch=master)
[![Forks](https://img.shields.io/github/forks/vyahello/movie-search-api)](https://github.com/vyahello/movie-search-api/network/members)
[![Stars](https://img.shields.io/github/stars/vyahello/movie-search-api)](https://github.com/vyahello/movie-search-api/stargazers)
[![Issues](https://img.shields.io/github/issues/vyahello/movie-search-api)](https://github.com/vyahello/movie-search-api/issues)

[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Hits-of-Code](https://hitsofcode.com/github/vyahello/movie-search-api)](https://hitsofcode.com/view/github/vyahello/movie-search-api)

# Movie search API
> A lightweight movie search API written in [responder](http://python-responder.org/en/latest/) python HTTP service framework. 
> Please follow https://movie-search-rest-api.herokuapp.com link app to see how it looks like.

**Tools/features**
> - python 3.7
> - responder
> - html5/css
> - pytest
> - shell
> - travis/github CI
> - heroku

## Table of contents
- [Usage](#usage)
- [Development notes](#development-notes)
  - [Run code analysis](#run-code-analysis)
  - [Heroku deployment](#heroku-deployment)
  - [Meta](#meta)
  - [Contributing](#contributing)

# Usage
Run script from the root directory of the project:
```bash
python movie_search_api.py
```

## Demo
![Screenshot](static/service.png)

# Development notes
## Run code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy`, and `unittests` accordingly.
To be able to start static code analysis _locally_ please run following script from the root directory of the project:
```bash
./run-code-analysis.sh install-dependencies
```

## Heroku deployment
Please follow instructions from - https://python-responder.org/en/latest/deployment.html

- Install heroku following by - https://devcenter.heroku.com/articles/heroku-cli#download-and-install
- Login to heroku
```bash
heroku login
```
- Create an application
```bash
heroku create movie-search-rest-api
```
- Commit and push repo into a heroku
```bash
git add . && git commit -m "My first heroku app" && git push heroku master
```
- Check heroku logs
```bash
heroku logs --tail
```
- Open an application via browser: https://movie-search-rest-api.herokuapp.com


## Release notes
* 0.2.0
    * Deploy application on heroku
* 0.1.0
    * Introduce initial app version

## Meta
Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

## Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development dependencies