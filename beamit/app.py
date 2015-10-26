from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from beamit.controllers.contact import create_contact_routes
from beamit.controllers.signup import create_signup_routes
from beamit.controllers.signin import create_signin_routes
from beamit.controllers.photo import create_photo_routes
from beamit.controllers.profile import create_profile_routes

app = Flask(__name__.split('.')[0])
app.debug = True
db = SQLAlchemy(app)
app.db = db

# Setup the routes
create_contact_routes(app)
create_signup_routes(app)
create_signin_routes(app)
create_photo_routes(app)
create_profile_routes(app)
