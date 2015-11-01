"""
password controller
"""
from flask import request
from json import dumps, loads
from requests import codes
from werkzeug.exceptions import NotFound, Unauthorized


from beamit.app import db
from beamit.model.profile import Profile
from beamit.resources.password import PasswordChangeRequest, PasswordChangeResponse


def create_password_routes(app):

    @app.route("/api/password", methods=["POST"])
    def change_password():
        pswd_change_request_resource = PasswordChangeRequest.from_dict(loads(request.get_data()))
        profile = Profile.query.filter_by(email=pswd_change_request_resource.email).first()
        if not profile:
            raise NotFound(
                "User not found for email ({})".format(pswd_change_request_resource.email),
            )
        if pswd_change_request_resource.password != profile.password:
            raise Unauthorized(
                "unauthorized user access for email({})".format(pswd_change_request_resource.email),
            )
        try:
            profile.password = pswd_change_request_resource.new_password
            db.session.commit()
            pswd_change = PasswordChangeResponse(profile.id)
            return dumps(pswd_change.to_dict()), codes.ok
        except Exception as e:
            app.logger.exception(e)
            db.session.rollback()
            raise
