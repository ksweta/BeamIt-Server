"""
Sign in controller
"""
from logging import getLogger
from json import dumps, loads

from beamit.resources.signin import SigninRequest, SigninResponse
from flask import request
from requests import codes


logger = getLogger(__name__)


def create_signin_routes(app):

    @app.route('/api/signin', methods=["POST"])
    def signin():
        logger.info("content-type: {}, data: {}".format(
            request.headers.get('content-type'),
            request.get_data(),
        ))

        signin_request = SigninRequest.from_dict(loads(request.get_data()))
        signin_response = SigninResponse("test-user-id")
        logger.info("signup_request: {}".format(signin_request, signin_response))
        return dumps(signin_response.to_dict()), codes.ok
