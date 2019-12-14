# Movie search API
A lightweight movie search API written in [_responder_](http://python-responder.org/en/latest/) python HTTP service framework. 
Please follow [movie search api](https://movie-search-rest-api.herokuapp.com) app to see how it looks like.

[![Build Status](https://travis-ci.org/vyahello/movie-search-api.svg?branch=master)](https://travis-ci.org/vyahello/movie-search-api)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/movie-search-api/badge.svg?branch=master)](https://coveralls.io/github/vyahello/movie-search-api?branch=master)

[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Hits-of-Code](https://hitsofcode.com/github/vyahello/movie-search-api)](https://hitsofcode.com/view/github/vyahello/movie-search-api)

## Table of contents
- [Run application](#run-application)
- [Demo](#demo)
- [Run static code analysis](#run-static-code-analysis)
- [Heroku deployment](#heroku-deployment)
- [Contributing](#contributing)

# Run application
Run script from the root directory of the project:
```bash
python movie_search_api.py
```

# Demo
![Screenshot](static/service.png)

# Run static code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy`, and `unittests` accordingly.
To be able to start static code analysis _locally_ please run following script from the root directory of the project:
```bash
./run-code-analysis.sh install-dependencies
```

# Heroku deployment
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


# Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.7+` is required to run the code
- `pip install -r requirements` to install all project dependencies
