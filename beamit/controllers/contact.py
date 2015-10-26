"""
contact controller
"""
from logging import getLogger
from json import dumps, loads

from beamit.resources.contact import Contact
from flask import request
from requests import codes


logger = getLogger(__name__)


def create_contact_routes(app):

    @app.route("/api/contact", methods=["POST"])
    def contact():
        logger.info("content-type: {}, data: {}".format(
            request.headers.get('content-type'),
            request.get_data(),
        ))

        contact = Contact.from_dict(loads(request.get_data()))
        contact.contact_id = "test-contact-id"
        logger.info("signup_request: {}".format(contact))
        return dumps(contact.to_dict()), codes.created

    @app.route("/api/contact/<contact_id>", methods=["GET"])
    def get_contact(contact_id):
        logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            contact_id,
        ))

        contact = Contact(
            user_id="test-user-id",
            contact_id=contact_id,
            name="kumari sweta",
            phone="5551112000",
            email="test@test.com",
            company="SFSU",
            linkedin_url="www.linked.com",
        )
        return dumps(contact.to_dict()), codes.ok

    @app.route("/api/contact/<contact_id>", methods=["DELETE"])
    def delete_contact(contact_id):
        logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            contact_id,
        ))

        return "", codes.ok
