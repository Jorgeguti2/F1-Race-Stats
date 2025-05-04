from flask import request
from flask_restx import Namespace, Resource, fields
from models import Drivers

# Driver namespace
driver_ns = Namespace('driver', description='A namespace for drivers.')

# Create a serializer to help us serialize our model into json format (Data that we can use in the frontend)
drivers_model = driver_ns.model(
    "Drivers",
    {
        "id": fields.Integer(),
        "name": fields.String(),
        "abbreviation": fields.String()
    }
)

# Defines all the various routes we are going to carry out with this specific route
@driver_ns.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello World"}

# Create different resource classes that are going to work with our model and help us access
# the different methods we are going to carry out
@driver_ns.route('/drivers')
class DriversResource(Resource):
    # Decorate this function with the serializer (marshal) to jsonify it
    @driver_ns.marshal_list_with(drivers_model)
    def get(self):
        """ Get all drivers """
        # Returns an SQLAlchemy object, so we need to jsonify it
        drivers = Drivers.query.all()
        return drivers

    # Responsible for creating the drivers
    # We use marshal with here instead of marshal list with because we are only returning one object
    @driver_ns.marshal_with(drivers_model)
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
@driver_ns.route('/drivers/<int:id>')
class DriverResource(Resource):
    @driver_ns.marshal_with(drivers_model)
    def get(self, id):
        """ Get a driver by id"""
        driver = Drivers.query.get_or_404(id)
        return driver

    @driver_ns.marshal_with(drivers_model)
    def put(self, id):
        """ Update a driver by id """
        driver_to_update = Drivers.query.get_or_404(id)
        data = request.get_json()
        driver_to_update.update(data.get('name'), data.get('abbreviation'))
        return driver_to_update

    @driver_ns.marshal_with(drivers_model)
    def delete(self, id):
        """ Delete a driver by id """
        driver_to_delete = Drivers.query.get_or_404(id)
        driver_to_delete.delete()
        return driver_to_delete


# Expose our model via these routes using our serializer using a specific decorator 
