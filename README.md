# talana-api

This is a REST API with [Django](https://docs.djangoproject.com/en/3.2/), [Django REST Framework](https://www.django-rest-framework.org/) and [Celery](https://docs.celeryproject.org/en/stable/).


## Overview: TALANA API

Problem Statement proposed by [TALANA](https://talana.com/)


## Table of Contents

* [Overview](#talana-api)
* [Main Dependencies](#Main-Dependencies)
* [Project Configuration](#Project-Configuration)


## Main Dependencies

    Python              ~3.8
    Django              ~3.2
    djangorestframework ~3.12
    PostgreSQL          ~12.7
    RabbitMQ            ~3.8
    Celery              ~5.1

For more details, see the [pyproject.toml file](pyproject.toml).

## Docker Configuration

- [Install Docker](https://docs.docker.com/engine/install/)

- [Install Docker Compose](https://docs.docker.com/compose/install/#install-compose)

## Project Configuration

- Clone this [repository](https://github.com/hugofer93/talana-api):

        $ git clone https://github.com/hugofer93/talana-api.git

- Create `.env` file based on `.env.sample`:

        $ cp .env.sample .env

    **Production or Staging Environment**:

    - Set `DEBUG=false`

    **Develop Environment**:

    - Set `DEBUG=true`

- Up Services with docker-compose:

    **Production or Staging Environment**:

        $ docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

    **Develop Environment**:

        $ docker-compose up -d

- Execute commands in container (e.g.):

        $ docker exec -it talana_api poetry run python manage.py createsuperuser

- Show containers logs:

    For Django Project:

        $ docker-compose logs -f api

    For Celery:

        $ docker-compose logs -f celery
