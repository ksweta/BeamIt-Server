"""
profile controller
"""
from flask import request
from json import dumps, loads
from requests import codes

from beamit.app import db
from beamit.model.profile import Profile
from beamit.resources.profile import Profile as ProfileResource


def create_profile_routes(app):

    @app.route("/api/profile", methods=["POST"])
    def profile():
        app.logger.info("content-type: {}, data: {}".format(
            request.headers.get('content-type'),
            request.get_data(),
        ))

        profile_resource = ProfileResource.from_dict(loads(request.get_data()))
        profile = Profile.from_profile_resource(profile_resource)
        try:
            db.session.add(profile)
            db.session.commit()
            return dumps(profile.to_profile_resource().to_dict()), codes.created
        except Exception as e:
            app.logger.exception(e)
            db.session.rollback()
            raise

    @app.route("/api/profile/<int:user_id>", methods=["GET"])
    def get_profile(user_id):
        app.logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            user_id,
        ))
        profile = Profile.query.get_or_404(user_id)
        return dumps(profile.to_profile_resource().to_dict()), codes.ok

    @app.route("/api/profile/<int:user_id>", methods=["DELETE"])
    def delete_profile(user_id):
        app.logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            user_id,
        ))
        profile = Profile.query.get_or_404(user_id)
        try:
            db.session.delete(profile)
            db.session.commit()
            return "", codes.ok
        except Exception as e:
            app.logger.exception(e)
            db.session.rollback()
            raise
