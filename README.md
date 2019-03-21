#### FLASK RESTFUL API BOILER-PLATE 

This is a full stack boilerplate project with flask restfull

+ flask
+ flask-restplus
+ SQLAlchemy
+ acra logger (internal feature added)

## Installation

Clone the repository and run `pip install` .

```
git clone https://github.com/ul2002/flask-rest-boilerplate.git
pip install -r requirements.txt

```


### Setting ###

    For windows users run 

    set APP_VERSION = <value>
    set APP_NAME = <value>
    set LOGGER_HOST = <value>
    set LOGGER_PORT = <value>
    set LOGGER_USER = <value>
    set LOGGER_PASSWORD = <value>

    For linux or mac users run 

    export APP_VERSION = <value>
    export APP_NAME = <value>
    export LOGGER_HOST = <value>
    export LOGGER_PORT = <value>
    export LOGGER_USER = <value>
    export LOGGER_PASSWORD = <value>


## Starting the server

```
python manage.py run
```

The server will run on port 5000. 

### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/

### Using logger ####

    The logger service is located at app/main/service/logger_service.py .
    The example below explain how to use it.

    from app.main.service.logger_service import logger
    log = logger()
    log.info('custom message')
    log.info('custom message',1) // write a log message only to local (level=info)
    log.error('custom message ')
    log.error('custom message ',1) // write a log message only to local (level=error)

```
https://github.com/ul2002/flask-rest-boilerplate.git
```
