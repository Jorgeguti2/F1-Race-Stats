from flask import Flask
from flask_restx import Api, Resource
from config import DevConfig

# Create an instance of the flask app
app = Flask(__name__)

# Set devconfig to work with our app
app.config.from_object(DevConfig)

# Create an instance of the api class
# Specify to it that the app to the api class is our current app
# Also specify the doc parameter that the url '/docs' is where our api docs are at
api = Api(app, doc='/docs')

# Defines all the various routes we are going to carry out with this specific route
@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello World"}

if __name__ == "__main__":
    app.run()
