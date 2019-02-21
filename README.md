#### FLASK RESTFUL API BOILER-PLATE 

### Terminal commands

    Initial installation: make install or pip install -r requirements.txt

    To run application: make run or python manage.py run


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### Using logger ####
    the logger service is located at app/main/service/logger_service.py
    the example below explain how to use it

    from app.main.service.logger_service import logger
    log = logger()
    log.info('custom message')
    log.info('custom message',1) // write a log message only to local (level=info)
    log.error('custom message ')
    log.error('custom message ',1) // write a log message only to local (level=error)

```
https://github.com/ul2002/flask-rest-boilerplate.git
```
