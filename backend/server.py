# Import necessary libraries
from flask import Flask

# Create app instance
app = Flask(__name__)

# Create a route for the members to reach member information
# Members API Route
@app.route("/members")
def members():
    # return a json array
    return {"members": ["Member1", "Member2", "Member3"]}

# runs the app
if __name__ == "__main__":
    # debug = true since we are in development mode
    app.run(debug=True)
