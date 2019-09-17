# Movie search API
A lightweight movie search API written in [_responder_](http://python-responder.org/en/latest/) python HTTP service framework.

[![Build Status](https://travis-ci.org/vyahello/movie-search-api.svg?branch=master)](https://travis-ci.org/vyahello/movie-search-api)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/movie-search-api/badge.svg?branch=master)](https://coveralls.io/github/vyahello/movie-search-api?branch=master)


## Table of contents
- [Run application](#run-application)
- [Demo](#demo)
- [Run static code analysis](#run-static-code-analysis)
- [Contributing](#contributing)

# Run application
Run script from the root directory of the project:
```bash
python search.py
```

# Demo
![Screenshot](static/service.png)

# Run static code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy`, and `unittests` accordingly.
To be able to start static code analysis _locally_ please run following script from the root directory of the project:
```bash
./run-code-analysis.sh install-dependencies
```

# Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6 +` is required to run the code
- `pip install -r requirements` to install all project dependencies
