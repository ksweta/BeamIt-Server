"""
profile controller
"""
from logging import getLogger
from json import dumps, loads

from beamit.resources.profile import Profile
from flask import request
from requests import codes


logger = getLogger(__name__)


def create_profile_routes(app):

    @app.route("/api/profile", methods=["POST"])
    def profile():
        logger.info("content-type: {}, data: {}".format(
            request.headers.get('content-type'),
            request.get_data(),
        ))

        profile = Profile.from_dict(loads(request.get_data()))
        profile.user_id = "test-user-id"
        logger.info("signup_request: {}".format(profile))
        return dumps(profile.to_dict()), codes.ok

    @app.route("/api/profile/<user_id>", methods=["GET"])
    def get_profile(user_id):
        logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            user_id,
        ))

        profile = Profile(
            user_id=user_id,
            name="kumari sweta",
            phone="5551112000",
            email="test@test.com",
            company="SFSU",
            linkedin_url="www.linked.com",
        )
        return dumps(profile.to_dict()), codes.ok

    @app.route("/api/profile/<user_id>", methods=["DELETE"])
    def delete_profile(user_id):
        logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            user_id,
        ))

        return "", codes.ok
