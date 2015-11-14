from os import environ
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__.split('.')[0])
app.debug = True

# App email. This email will be used to email.
app.config['APP_EMAIL'] = 'beamit-support@heroku.com'
app.config['ANDROID_APP_DOWNLOAD_LINK'] = 'https://blooming-cliffs-9672.herokuapp.com/android/download'

# Adding db configuration. Select the UIR based on the requirement
if environ.get('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
    app.config['SENDGRID_USERNAME'] = environ.get('SENDGRID_USERNAME')
    app.config['SENDGRID_PASSWORD'] = environ.get('SENDGRID_PASSWORD')

else:
    from beamit.config import (
        SENDGRID_PASSWORD,
        SENDGRID_USERNAME,
        SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_ECHO,
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_ECHO'] = SQLALCHEMY_ECHO
    app.config['SENDGRID_USERNAME'] = SENDGRID_USERNAME
    app.config['SENDGRID_PASSWORD'] = SENDGRID_PASSWORD

# Set database
db = SQLAlchemy(app)

from beamit.controllers.contact import create_contact_routes  # noqa
from beamit.controllers.invite import create_invite_routes  # noqa
from beamit.controllers.landing_page import create_landing_page_routes  # noqa
from beamit.controllers.signup import create_signup_routes  # noqa
from beamit.controllers.signin import create_signin_routes  # noqa
from beamit.controllers.password import create_password_routes  # noqa
from beamit.controllers.photo import create_photo_routes  # noqa
from beamit.controllers.user import create_user_routes  # noqa


# These need to be here otherwose db.create_all() will not work
from beamit.model.user import User  # noqa
from beamit.model.contact import Contact  # noqa


# Setup the routes
create_contact_routes(app)
create_invite_routes(app)
create_landing_page_routes(app)
create_signup_routes(app)
create_signin_routes(app)
create_password_routes(app)
create_photo_routes(app)
create_user_routes(app)
