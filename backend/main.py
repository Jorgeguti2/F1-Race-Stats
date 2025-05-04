from flask import Flask
from flask_restx import Api
from  models import Drivers
from exts import db
from flask_migrate import Migrate
from drivers import driver_ns

# Create an app function that creates the app and returns it
def create_app(config):

    # Create an instance of the flask app
    app = Flask(__name__)

    # Set devconfig to work with our app
    app.config.from_object(config)

    # Initialize db instance to register it with our application
    db.init_app(app)

    # Make sure we instantiate flask migrate to work with the app
    # Helps create a migration repository that keeps track of all db changes/versions
    migrate = Migrate(app, db)

    # Create an instance of the api class
    # Specify to it that the app to the api class is our current app
    # Also specify the doc parameter that the url '/docs' is where our api docs are at
    api = Api(app, doc='/docs')
    # add the drivers namespace to the api
    api.add_namespace(driver_ns)

    # Create a context processor to help us access our model and db instance within our terminal
    # Helps us interact with our database objects
    @app.shell_context_processor
    def make_shell_context():
        return {
            "db": db,
            "Drivers": Drivers
        }

    return app
