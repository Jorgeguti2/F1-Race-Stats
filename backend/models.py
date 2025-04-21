# This file is to create the database model
from exts import db

# from the import db instance, we are going to create our model
class Drivers(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(), nullable=False)
    abbreviation = db.Column(db.String(), nullable=False)

    # Create some continuous methods to help us create crud operations onto our Drivers model class
    # Helps return string represented objects
    def __repr__(self):
        return f"<Drivers {self.name} >"

    # Works on the current object and adds it to the database
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Create a method to delete the current object
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # Create a method to update the current object
    def update(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        db.session.commit()
