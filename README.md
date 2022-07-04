# Strawberry Django Subscriptions

This is an example project to accompany a Medium article I wrote.

To run it, you'll want to clone the project and run these commands in it's directory

```shell
docker run -p 6379:6379 -d redis
pipenv sync
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```