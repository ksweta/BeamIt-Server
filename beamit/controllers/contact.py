"""
contact controller
"""
from flask import request
from json import dumps, loads
from requests import codes
from werkzeug.exceptions import BadRequest

from beamit.app import db
from beamit.model.contact import Contact
from beamit.model.user import User
from beamit.resources.contact import Contact as ContactResource, ContactList


def parse_int_arg(name):
    value = request.args.get(name)
    if value is None:
        return None
    try:
        return int(value)
    except ValueError:
        raise BadRequest("{} is not a valid integer".format(name))


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
        app.logger.info("content-type: {}, contact_id: {}".format(
            request.headers.get('content-type'),
            contact_id,
        ))

        contact = Contact.query.get_or_404(contact_id)
        return dumps(contact.to_contact_resource().to_dict()), codes.ok

    @app.route("/api/contact/<int:contact_id>", methods=["DELETE"])
    def delete_contact(contact_id):
        app.logger.info("content-type: {}, contact_id: {}".format(
            request.headers.get('content-type'),
            contact_id,
        ))
        contact = Contact.query.get_or_404(contact_id)
        db.session.delete(contact)
        db.session.commit()
        return "", codes.no_content

    @app.route("/api/contactlist/user/<int:owner_id>", methods=["GET"])
    def get_contacts_for_user(owner_id):
        record_offset = parse_int_arg("offset") or 0
        # if limit is None that means return all contacts.
        record_limit = parse_int_arg("limit")
        app.logger.info("owner_id (user_id): {}, offset: {}, limit: {}",
                        owner_id,
                        record_offset,
                        record_limit)

        # Make sure owner exists
        User.query.get_or_404(owner_id)
        if record_limit:
            contacts = Contact.query.filter_by(owner_id=owner_id).limit(record_limit).offset(record_offset).all()  # noqa
        else:
            contacts = Contact.query.filter_by(owner_id=owner_id).offset(record_offset).all()

        contact_list = ContactList(items=[contact.to_contact_resource() for contact in contacts],
                                   offset=record_offset,
                                   limit=record_limit,
                                   total_count=len(contacts))

        return dumps(contact_list.to_dict()), codes.ok
