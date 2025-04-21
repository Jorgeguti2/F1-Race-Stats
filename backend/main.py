from flask import Flask, request
from flask_restx import Api, Resource, fields
from config import DevConfig
from  models import Drivers
from exts import db

# Create an instance of the flask app
app = Flask(__name__)

# Set devconfig to work with our app
app.config.from_object(DevConfig)

# Initialize db instance to register it with our application
db.init_app(app)

# Create an instance of the api class
# Specify to it that the app to the api class is our current app
# Also specify the doc parameter that the url '/docs' is where our api docs are at
api = Api(app, doc='/docs')

# Create a serializer to help us serialize our model into json format (Data that we can use in the frontend)
drivers_model = api.model(
    "Drivers",
    {
        "id": fields.Integer(),
        "name": fields.String(),
        "abbreviation": fields.String()
    }
)

# Defines all the various routes we are going to carry out with this specific route
@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello World"}

# Create different resource classes that are going to work with our model and help us access
# the different methods we are going to carry out
@api.route('/drivers')
class DriversResource(Resource):
    # Decorate this function with the serializer (marshal) to jsonify it
    @api.marshal_list_with(drivers_model)
    def get(self):
        """ Get all drivers """
        # Returns an SQLAlchemy object, so we need to jsonify it
        drivers = Drivers.query.all()
        return drivers

    # Responsible for creating the drivers
    # We use marshal with here instead of marshal list with because we are only returning one object
    @api.marshal_with(drivers_model)
    def post(self):
        """ Create a new driver """
        # To access data from our json or coming from any client
        data = request.get_json()

        new_driver = Drivers(
            name = data.get('name'),
            abbreviation = data.get('abbreviation')
        )

        new_driver.save()
        return new_driver,201

# Create a route to help us delete, update, and get one specfic driver
@api.route('/drivers/<int:id>')
class DriverResource(Resource):
    @api.marshal_with(drivers_model)
    def get(self, id):
        """ Get a driver by id"""
        driver = Drivers.query.get_or_404(id)
        return driver

    @api.marshal_with(drivers_model)
    def put(self, id):
        """ Update a driver by id """
        driver_to_update = Drivers.query.get_or_404(id)
        data = request.get_json()
        driver_to_update.update(data.get('name'), data.get('abbreviation'))
        return driver_to_update

    @api.marshal_with(drivers_model)
    def delete(self, id):
        """ Delete a driver by id """
        driver_to_delete = Drivers.query.get_or_404(id)
        driver_to_delete.delete()
        return driver_to_delete


# Expose our model via these routes using our serializer using a specific decorator 

# Create a context processor to help us access our model and db instance within our terminal
# Helps us interact with our database objects
@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Drivers": Drivers
    }

if __name__ == "__main__":
    app.run()
