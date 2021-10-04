# Wheater API
An API that provides the wheater from a city around the world.

In this example you can GET the wheater payload from all the cities. Also you can query in url by city and date fields or, you can even combine this filter and sorte by date field.

Example of a information that the API brings to you
```
    "id": 1,
    "date": "2019-06-11",
    "lat": 41.8818,
    "lon": -87.6231,
    "city": "Oakland",
    "state": "California",
    "temperatures": [24.0, 21.5, 24.0, 19.5, 25.5]
```

Before you start, make sure you have python ^3.9 installed and the poetry package too.

For better experience, its recomended that you use [pyenv](https://github.com/pyenv/pyenv) to managing you python versions

To install poetry, please check the [documentation](https://python-poetry.org/docs/)

After that, you can clone the repository

```
$ git clone git@github.com:pauloestrella1994/wheater_api.git
```

install the dependencies
```
poetry install
```

Make sure you have you .env file configurated with you secret key, you can copy the local.env template and change the secret value

```
cp local.env .env
```

Migrate the database to add a db.sqlite3 and you can load some data to start to use you API
```
poetry run python manage.py migrate
poetry run python manage.py loaddata data.json
```

Finally, run the server:
```
poetry run python manage.py runserver
```

The tests
```
poetry run pytest --cov -sx -v
```
