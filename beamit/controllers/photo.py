from flask import send_file
from logging import getLogger
from requests import codes

logger = getLogger(__name__)


def create_photo_routes(app):

    @app.route('/photo')
    def get_photo():
        try:
            logger.info("Get logger")
            result = send_file('./controllers/flask.png', mimetype='image/png')
            logger.info(result)
            return result
        except Exception as error:
            logger.exception(error)
        return "hello there from photo", codes.ok
