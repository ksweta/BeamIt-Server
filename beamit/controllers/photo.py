from flask import request, Response, send_file
from requests import codes

from beamit.app import db
from beamit.model.profile import Profile
from beamit.model.contact import Contact


def create_photo_routes(app):

    @app.route('/api/photo')
    def get_photo():
        try:
            app.logger.info("Get logger")
            result = send_file('./controllers/sfsu.jpg', mimetype='image/jpg')
            return result, codes.ok
        except Exception as error:
            app.logger.exception(error)
            raise error

    @app.route('/api/photo/user/<int:user_id>', methods=["POST"])
    def post_user_photo(user_id):
        app.logger.info("post_user_photo=> user_id:{}, photo: {}".format(
            user_id,
            request.files['photo'].filename,
        ))
        profile = Profile.query.get_or_404(user_id)
        try:
            profile.photo = request.files['photo'].read()
        except Exception as e:
            app.logger.exception(e)
            db.session.rollback()
            raise
        db.session.commit()
        return "{}: {}".format(user_id, request.files['photo'].filename), codes.ok

    @app.route('/api/photo/user/<int:user_id>', methods=["GET"])
    def get_profile_photo(user_id):
        app.logger.info("get_profile_photo=> user_id: {}".format(user_id))
        profile = Profile.query.get_or_404(user_id)
        return Response(profile.photo, mimetype='image/png')

    @app.route('/api/photo/contact/<int:contact_id>', methods=["GET"])
    def get_contact_photo(contact_id):
        app.logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            contact_id,
        ))
        app.logger.info("get_contact_photo=>  contact_id: {}".format(contact_id))
        contact = Contact.query.get_or_404(contact_id)
        return Response(contact.photo, mimetype='image/png')

    @app.route('/api/photo/contact/<int:contact_id>', methods=["POST"])
    def post_contact_photo(contact_id):
        app.logger.info("post_contact_photo=> contact_id: {}, photo: {}".format(
            contact_id,
            request.files['photo'].filename
        ))
        contact = Contact.query.get_or_404(contact_id)
        try:
            contact.photo = request.files['photo'].read()
        except Exception as e:
            app.logger.exception(e)
            db.session.rollback()
            raise

        db.session.commit()
        return "{}: {}".format(contact_id, request.files['photo'].filename), codes.ok
