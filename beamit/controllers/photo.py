from flask import request, send_file
from logging import getLogger
from requests import codes

logger = getLogger(__name__)


def create_photo_routes(app):

    @app.route('/api/photo')
    def get_photo():
        try:
            logger.info("Get logger")
            result = send_file('./controllers/flask.png', mimetype='image/png')
            logger.info(result)
            return result
        except Exception as error:
            logger.exception(error)
        return "hello there from photo", codes.ok

    @app.route('/api/photo/user/<user_id>', methods=["GET"])
    def get_profile_photo(user_id):
        logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            user_id,
        ))
        logger.info("Get logger")
        result = send_file('./controllers/flask.png', mimetype='image/png')
        logger.info(result)
        return result, codes.ok

    @app.route('/api/photo/contact/<contact_id>', methods=["GET"])
    def get_contact_photo(contact_id):
        logger.info("content-type: {}, user_id: {}".format(
            request.headers.get('content-type'),
            contact_id,
        ))
        logger.info("Get logger")
        result = send_file('./controllers/flask.png', mimetype='image/png')
        logger.info(result)
        return result, codes.ok
