This is the API backend for the Monuments app.

## QUICKSTART

1. create a virtualenv with Python 3.4
2. activate the virtualenv and do `pip install -r requirements.txt`
3. `./manage.py migrate`
4. `.manage.py runserver`

Go to localhost:8000/monuments/<some number> -- at this point it doesn't matter which, there are no objects to look up, but eventually the number will be a given monument's ID. 