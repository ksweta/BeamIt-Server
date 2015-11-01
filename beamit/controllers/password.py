"""
password controller
"""
from flask import request
from json import dumps, loads
from requests import codes
from werkzeug.exceptions import NotFound, Unauthorized


from beamit.app import db
from beamit.model.user import User
from beamit.resources.password import PasswordChangeRequest, PasswordChangeResponse


def create_password_routes(app):

    @app.route("/api/password", methods=["POST"])
    def change_password():
        pswd_change_request_resource = PasswordChangeRequest.from_dict(loads(request.get_data()))
        user = User.query.filter_by(email=pswd_change_request_resource.email).first()
        if not user:
            raise NotFound(
                "User not found for email ({})".format(pswd_change_request_resource.email),
            )
        if pswd_change_request_resource.password != user.password:
            raise Unauthorized(
                "unauthorized user access for email({})".format(pswd_change_request_resource.email),
            )
        try:
            user.password = pswd_change_request_resource.new_password
            db.session.commit()
            pswd_change = PasswordChangeResponse(user.id)
            return dumps(pswd_change.to_dict()), codes.ok
        except Exception as e:
            app.logger.exception(e)
            db.session.rollback()
            raise
