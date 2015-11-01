"""
Signup controller
"""
from flask import request
from json import dumps, loads
from requests import codes
from werkzeug.exceptions import Conflict

from beamit.app import db
from beamit.resources.signup import SignupRequest, SignupResponse
from beamit.model.user import User


def create_signup_routes(app):

    @app.route('/')
    def root():
        return 'Hello from BeamIt!!'

    @app.route("/api/signup", methods=["POST"])
    def signup():
        app.logger.info("content-type: {}, data: {}".format(
            request.headers.get('content-type'),
            request.get_data(),
        ))

        signup_request_resource = SignupRequest.from_dict(loads(request.get_data()))
        user = User.query.filter_by(email=signup_request_resource.email).first()
        if user:
            raise Conflict(
                "User already exists for email ({})".format(signup_request_resource.email),
            )

        user = User(signup_request_resource.email, signup_request_resource.password)

        try:
            db.session.add(user)
            db.session.commit()
            signup_response = SignupResponse(user.id)
            app.logger.info("signup request: {}, response: {}".format(
                signup_request_resource,
                signup_response,
            ))
            return dumps(signup_response.to_dict()), codes.created
        except Exception as e:
            app.logger.exception(e)
            db.session.rollback()
            raise
