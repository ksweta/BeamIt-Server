"""
Sign in controller
"""
from flask import request
from json import dumps, loads
from requests import codes
from werkzeug.exceptions import NotFound, Unauthorized


from beamit.model.user import User
from beamit.resources.signin import SigninRequest, SigninResponse


def create_signin_routes(app):

    @app.route('/api/signin', methods=["POST"])
    def signin():
        app.logger.info("content-type: {}, data: {}".format(
            request.headers.get('content-type'),
            request.get_data(),
        ))

        signin_request_resource = SigninRequest.from_dict(loads(request.get_data()))
        user = User.query.filter_by(email=signin_request_resource.email).first()
        if not user:
            raise NotFound(
                "User not found for email ({})".format(signin_request_resource.email),
            )

        if signin_request_resource.password != user.password:
            raise Unauthorized(
                "unauthorized user access for email({})".format(signin_request_resource.email),
            )

        signin_response = SigninResponse(user.id)
        return dumps(signin_response.to_dict()), codes.ok
