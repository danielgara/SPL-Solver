import os
import unittest

from flask_script import Manager

from solvers.main.controller import cnf
from solvers.main import create_app

app = create_app(os.getenv("APP_CONFIG", "dev"))
app.app_context().push()


# Register Blueprints
app.register_blueprint(cnf.blueprint, url_prefix='/solvers/cnf')

# Print URLs
print(app.url_map)

manager = Manager(app)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
