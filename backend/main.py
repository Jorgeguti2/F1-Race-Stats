from flask import Flask
from flask_restx import Api, Resource

# Create an instance of the flask app
app = Flask(__name__)

# Create an instance of the api class
# Specify to it that the app to the api class is our current app
# Also specify the doc that the url '/docs' is where our api docs are at
api = Api(app, doc='/docs')

# 
@api.route('/hello')
class
