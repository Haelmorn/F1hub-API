# F1-hub backend

This app was created to provide a backend to f1-hub app.
It is a simple Django+graphene setup, based on an existing mySQL database, which can be found at http://ergast.com/mrd/db/

The API can be accessed at: https://safe-bayou-28242.herokuapp.com/graphql/

## Running 

To run the server, you will need to first install all the dependencies. To do so, create and activate a python virtual environment by executing
```
python3.6 -m venv venv
source venv/bin/activate
```
Then, execute:
```
pip install django==2.1.4 graphene-django==2.2.0 django-filter==2.0.0 django-graphql-jwt==0.1.5
cd f1hub/
python manage.py runserver
```
To install all necessary packages and run the server.
From this point on, the server will be available at 127.0.0.1:8000.

## Testing

To test making queries, you can either use a third-party REST client (I recommend [Insomnia](https://insomnia.rest/)) or visit http://127.0.0.1:8000/graphql and use the in-build system.
