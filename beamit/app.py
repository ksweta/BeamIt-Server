from flask import Flask


from beamit.controllers.signup import create_signup_routes
from beamit.controllers.photo import create_photo_routes

app = Flask(__name__.split('.')[0])
app.debug = True

# Setup the routes
create_signup_routes(app)
create_photo_routes(app)
