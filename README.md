# talana-api

This is a REST API with [Django](https://docs.djangoproject.com/en/3.2/), [Django REST Framework](https://www.django-rest-framework.org/) and [Celery](https://docs.celeryproject.org/en/stable/).


## Overview: TALANA API

Problem Statement proposed by [TALANA](https://talana.com/)


## Table of Contents

* [Overview](#talana-api)
* [Main Dependencies](#Main-Dependencies)
* [Python Configuration](#Python-Configuration)
* [Project Configuration](#Project-Configuration)


## Main Dependencies

    Python              ~3.8
    Django              ~3.2
    djangorestframework ~3.12
    Celery              ~5.1

For more details, see the [pyproject.toml file](pyproject.toml).

## Python Configuration

- [Install Pyenv](https://github.com/pyenv/pyenv-installer)
- Install Python ~3.8:

    If you want to see **all available versions of Python**:

        $ pyenv install --list

    Now install the version you want of Python 3.8. e.g.:

        $ pyenv install 3.8.10

- [Install Poetry](https://python-poetry.org/docs/#installation)

- Configure the creation of the **virtual environment within the project:**

        $ vim $HOME/.bashrc

    **Add these lines to the end of the file:**

        # Poetry
        export POETRY_VIRTUALENVS_IN_PROJECT=1

## Project Configuration

- Clone this [repository](https://github.com/hugofer93/talana-api):

        $ git clone https://github.com/hugofer93/talana-api.git

- Create `.env` file based on `.env.sample`:

        $ cp .env.sample .env

- **Activate the installed Python 3.8 version**. e.g.:

        $ pyenv shell 3.8.10

- Install dependencies **in Production environment:**

        $ poetry install --no-dev

    **For Development environment:**

        $ poetry install

- Activate virtual environment (optional):

        $ poetry shell

    Alternatively you can run without activating the virtual environment:

        $ poetry run <commands described below>

    e.g.:

        $ poetry run python file.py

- If you are in development environment:

        $ python manage.py runserver

    In another terminal, run the celery worker:

        $ celery -A talana worker -l INFO
