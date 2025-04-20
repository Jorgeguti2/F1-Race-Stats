# This file is to create the database model
from exts import db

# from the import db instance, we are going to create our model
class Driver(db.Model):
    id = db.Column(db.String(), primary_key = True)
    name = db.Column(db.String(), nullable=False)
