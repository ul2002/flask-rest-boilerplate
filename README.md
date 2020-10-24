#### FLASK RESTFUL API BOILER-PLATE 

This is a full stack boilerplate project with flask restfull 

+ flask
+ flask-restplus
+ SQLAlchemy
+ PMA
+ logger (internal feature added)

## Installation

Clone the repository and run `pip install`

```
git clone https://github.com/ul2002/flask-rest-boilerplate.git
pip install -r requirements.txt

```


### Setting ###

For windows users run 

set FLASK_APP = <value>

For linux or mac users run 

export FLASK_APP = <value>


## Starting the server

```
python manage.py run
```

## Run migration

```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
## With Docker
```
docker-compose build .
docker-compose up -d
```

The server will run on port 5000. 

### Viewing the app ###

Open the following url on your browser to view swagger documentation
http://127.0.0.1:5000/

```
https://github.com/ul2002/flask-rest-boilerplate.git
```
