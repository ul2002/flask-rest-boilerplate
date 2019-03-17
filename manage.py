import os
import unittest

from flask_script import Manager

from app import blueprint
from app.main import create_app
from app.main.service.logger_service import logger

app = create_app('dev')

log = logger()
#log.info('Server started ');

app.register_blueprint(blueprint)

app.app_context().push()



manager = Manager(app)

@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
