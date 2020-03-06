import os
import unittest

from flask_script import Manager

from solvers.main import controller
from solvers.main import create_app
from solvers.main.controller import solver


app = create_app(os.getenv("APP_CONFIG", "dev"))
app.app_context().push()

# Register Blueprints
app.register_blueprint(controller.solver.solver_blueprint)

manager = Manager(app)


@manager.command
def run():
    app.run()


@manager.command
def test():
    tests = unittest.TestLoader() \
                    .discover("solvers/test", pattern="test_*.py")

    result = unittest.TextTestRunner(verbosity=2) \
                     .run(tests)

    if result.wasSuccessful():
        return 0

    return 1


if __name__ == '__main__':
    manager.run()
