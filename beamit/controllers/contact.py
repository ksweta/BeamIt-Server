"""
contact controller
"""
from flask import request
from json import dumps, loads
from requests import codes

from beamit.app import db
from beamit.model.contact import Contact
from beamit.model.user import User
from beamit.resources.contact import Contact as ContactResource


def create_contact_routes(app):

    @app.route("/api/contact", methods=["POST"])
    def contact():
        app.logger.info("content-type: {}, data: {}".format(
            request.headers.get('content-type'),
            request.get_data(),
        ))

        contact_resource = ContactResource.from_dict(loads(request.get_data()))
        # Make sure user exists
        User.query.get_or_404(contact_resource.owner_id)
        contact_model = Contact.from_contact_resource(contact_resource)
        try:
            db.session.add(contact_model)
            db.session.commit()
            contact_resource = contact_model.to_contact_resource()
            return dumps(contact_resource.to_dict()), codes.created
        except Exception as e:
            app.logger.exception(e)
            db.session.rollback()
            raise

    @app.route("/api/contact/<int:contact_id>", methods=["GET"])
    def get_contact(contact_id):
        app.logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            contact_id,
        ))

        contact = Contact.query.get_or_404(contact_id)
        return dumps(contact.to_contact_resource().to_dict()), codes.ok

    @app.route("/api/contact/<contact_id>", methods=["DELETE"])
    def delete_contact(contact_id):
        app.logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            contact_id,
        ))
        contact = Contact.query.get_or_404(contact_id)
        db.session.delete(contact)
        db.session.commit()
        return "", codes.no_content
