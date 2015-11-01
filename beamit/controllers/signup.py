"""
Signup controller
"""
from json import dumps, loads

from beamit.resources.signup import SignupRequest, SignupResponse
from flask import request
from requests import codes


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

        signup_request = SignupRequest.from_dict(loads(request.get_data()))
        signup_response = SignupResponse("test-user-id")
        app.logger.info("signup_request: {}".format(signup_request, signup_response))
        return dumps(signup_response.to_dict()), codes.created
