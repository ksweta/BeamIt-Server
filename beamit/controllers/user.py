"""
User controller
"""
from flask import request
from json import dumps, loads
from requests import codes

from beamit.app import db
from beamit.model.user import User
from beamit.model.contact import Contact
from beamit.resources.user import User as UserResource


def create_user_routes(app):

    @app.route("/api/user", methods=["POST"])
    def create_user():
        app.logger.info("content-type: {}, data: {}".format(
            request.headers.get('content-type'),
            request.get_data(),
        ))

        user_resource = UserResource.from_dict(loads(request.get_data()))
        user = User.from_user_resource(user_resource)
        try:
            db.session.add(user)
            db.session.commit()
            return dumps(user.to_user_resource().to_dict()), codes.created
        except Exception as e:
            app.logger.exception(e)
            db.session.rollback()
            raise

    @app.route("/api/user", methods=["PUT"])
    def update_user():
        app.logger.info("content-type: {}, data: {}".format(
            request.headers.get('content-type'),
            request.get_data(),
        ))

        user_resource = UserResource.from_dict(loads(request.get_data()))
        user = User.query.get_or_404(user_resource.id)
        try:
            user.email = user_resource.email
            user.name = user_resource.name
            user.phone = user_resource.phone
            user.company = user_resource.company
            user.linkedin_url = user_resource.linkedin_url
            db.session.commit()
            return dumps(user.to_user_resource().to_dict()), codes.ok
        except Exception as e:
            app.logger.exception(e)
            db.session.rollback()
            raise

    @app.route("/api/user/<int:user_id>", methods=["GET"])
    def get_user(user_id):
        app.logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            user_id,
        ))
        user = User.query.get_or_404(user_id)
        return dumps(user.to_user_resource().to_dict()), codes.ok

    @app.route("/api/user/<int:user_id>", methods=["DELETE"])
    def delete_user(user_id):
        app.logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            user_id,
        ))
        user = User.query.get_or_404(user_id)
        contacts = Contact.query.filter_by(owner_id=user.id)
        try:
            for contact in contacts:
                db.session.delete(contact)
            db.session.delete(user)
            db.session.commit()
            return "", codes.no_content
        except Exception as e:
            app.logger.exception(e)
            db.session.rollback()
            raise
