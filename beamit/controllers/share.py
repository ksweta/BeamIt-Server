"""
Share controller
"""
from flask import request
from json import dumps, loads
from requests import codes

from beamit.app import db
from beamit.model.contact import Contact
from beamit.model.user import User
from beamit.resources.share import Share


def create_share_routes(app):

    @app.route("/api/share", methods=["POST"])
    def share_contact():
        app.logger.info("data: {}".format(
            request.get_data(),
        ))

        share = Share.from_dict(loads(request.get_data()))

        owner_user = User.query.get_or_404(share.owner_id)
        subject_user_model = User.query.get_or_404(share.subject_id)

        contact_model = Contact(
            owner_id=owner_user.id,
            email=subject_user_model.email,
            name=subject_user_model.name,
            phone=subject_user_model.phone,
            company=subject_user_model.company,
            linkedin_url=subject_user_model.linkedin_url,
            photo=subject_user_model.photo,
        )
        try:
            db.session.add(contact_model)
            db.session.commit()
            contact_resource = contact_model.to_contact_resource()
            return dumps(contact_resource.to_dict()), codes.created
        except Exception as error:
            app.logger.exception(error)
            db.session.rollback()
            raise
