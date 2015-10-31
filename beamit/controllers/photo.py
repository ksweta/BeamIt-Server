from flask import request, Response, send_file
from logging import getLogger
from requests import codes

from beamit.app import db
from beamit.model.profile import Profile

logger = getLogger(__name__)


def create_photo_routes(app):

    @app.route('/api/photo')
    def get_photo():
        try:
            logger.info("Get logger")
            result = send_file('./controllers/sfsu.jpg', mimetype='image/jpg')
            logger.info(result)
            return result
        except Exception as error:
            logger.exception(error)
        return "hello there from photo", codes.ok

    @app.route('/api/photo/user/<int:user_id>', methods=["POST"])
    def post_user_photo(user_id):
        # print request.files['photo'].filename, codes.ok
        logger.info("{}: {}".format(user_id, request.files['photo'].filename))
        try:
            profile = db.session.query(Profile).get(user_id)
            profile.photo = request.files['photo'].read()
        except Exception as e:
            logger.info(e)
            db.session.rollback()
        db.session.commit()
        return "{}: {}".format(user_id, request.files['photo'].filename), codes.ok

    @app.route('/api/photo/user/<int:user_id>', methods=["GET"])
    def get_profile_photo(user_id):
        logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            user_id,
        ))
        logger.info("Get logger")
        # result = send_file('./controllers/sfsu.jpg', mimetype='image/png')
        # logger.info(result)
        profile = db.session.query(Profile).get(user_id)
        return Response(profile.photo, mimetype='image/png')

    @app.route('/api/photo/contact/<contact_id>', methods=["GET"])
    def get_contact_photo(contact_id):
        logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            contact_id,
        ))
        logger.info("Get logger")
        result = send_file('./controllers/sfsu.jpg', mimetype='image/png')
        logger.info(result)
        return result, codes.ok

    @app.route('/api/photo/contact/<contact_id>', methods=["POST"])
    def post_contact_photo(contact_id):
        # import ipdb; ipdb.set_trace()
        print request.files['photo'].filename, codes.ok
        return "{}: {}".format(contact_id, request.files['photo'].filename), codes.ok
