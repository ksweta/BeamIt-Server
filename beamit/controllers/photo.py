from flask import request, Response, send_file
from requests import codes

from beamit.app import db
from beamit.model.user import User
from beamit.model.contact import Contact


def create_photo_routes(app):

    @app.route('/api/photo')
    def get_photo():
        """
        This is just a test method api. It will be removed in future.
        """
        try:
            app.logger.info("Get logger")
            result = send_file('./resources/static/sfsu.jpg', mimetype='image/jpg')
            return result, codes.ok
        except Exception as error:
            app.logger.exception(error)
            raise error

    @app.route('/api/photo/user/<int:user_id>', methods=["GET"])
    def get_user_photo(user_id):
        app.logger.info("get_user_photo=> user_id: {}".format(user_id))
        user = User.query.get_or_404(user_id)
        return Response(user.photo, mimetype='image/png')

    @app.route('/api/photo/user/<int:user_id>', methods=["POST"])
    def post_user_photo(user_id):
        app.logger.info("post_user_photo=> user_id:{}, photo: {}".format(
            user_id,
            request.files['photo'].filename,
        ))
        user = User.query.get_or_404(user_id)
        try:
            user.photo = request.files['photo'].read()
        except Exception as e:
            app.logger.exception(e)
            db.session.rollback()
            raise
        db.session.commit()
        return "", codes.no_content

    @app.route('/api/photo/contact/<int:contact_id>', methods=["GET"])
    def get_contact_photo(contact_id):
        app.logger.info("content-type: {}, contact_id: {}".format(
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
        return "", codes.ok
