"""
Invite controller
"""
from flask import request
from json import loads
from requests import codes
from sendgrid import Mail, SendGridClient
from werkzeug.exceptions import InternalServerError


from beamit.model.user import User
from beamit.resources.invite import EmailInvite


def create_invite_routes(app):

    def send_email(user, invitee_email):
        sgc = SendGridClient(app.config.get("SENDGRID_USERNAME"),
                             app.config.get("SENDGRID_PASSWORD"))
        app_email = app.config.get('APP_EMAIL')
        android_download_link = app.config.get('ANDROID_APP_DOWNLOAD_LINK')
        email_subject = "Try Beamit Android Application"
        email_content = "{}({}) has invited you to try BeamIt application. \
            Please download it from here({}).".format(
            user.name,
            user.email,
            android_download_link)

        mail = Mail()
        mail.add_to(invitee_email)
        mail.set_from(app_email)
        mail.set_subject(email_subject)
        mail.set_text(email_content)
        status, response = sgc.send(mail)
        app.logger.info("sendgrid status code: {}, response: {}".format(status, response))
        if status != codes.ok:
            # Minimal error check
            raise InternalServerError("Couldn't send email: {}".format(response))

        return "", status

    @app.route('/api/invite/email', methods=['POST'])
    def email_invite():
        app.logger.info("content-type: {}, data: {}".format(
            request.headers.get('content-type'),
            request.get_data(),
        ))
        email_invite = EmailInvite.from_dict(loads(request.get_data()))
        # Make sure user_id does exits
        user = User.query.get_or_404(email_invite.user_id)

        return send_email(user, email_invite.invitee_email)
