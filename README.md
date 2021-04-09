# django-aws-cognito-example

Example of integration AWS Cognito with Django

# How to use it?

1. Create `.env` in `config` directory (`.env.template` is present)
2. `docker-compose build`
3. `docker-compose run --rm web python manage.py migrate`
4. `docker-compose up`
5. Navigate browser to `http://localhost:8000/accounts/login/'
6. Click on `Amazon Cognito` to start auth process

---

This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template). Current template version is: [53c67cf2c27f8d8cdd61710bcda31f6876c6d68d](https://github.com/wemake-services/wemake-django-template/tree/53c67cf2c27f8d8cdd61710bcda31f6876c6d68d). See what is [updated](https://github.com/wemake-services/wemake-django-template/compare/53c67cf2c27f8d8cdd61710bcda31f6876c6d68d...master) since then.


[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services) 
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)


## Prerequisites

You will need:

- `python3.8` (see `pyproject.toml` for full version)
- `postgresql` with version `9.6`
- `docker` with [version at least](https://docs.docker.com/compose/compose-file/#compose-and-docker-compatibility-matrix) `18.02`


## Development

When developing locally, we use:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- [`poetry`](https://github.com/python-poetry/poetry) (**required**)
- `pycharm 2017+` or `vscode`

## Credits

Sponsored by [Welltory](https://welltory.com)