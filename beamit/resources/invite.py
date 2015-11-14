from beamit.resources.base import Resource


class EmailInvite(Resource):

    MEDIA_TYPE = 'application/vnd.beamit.invite.email+json'

    def __init__(self, user_id, invitee_email):
        self.user_id = user_id
        self.invitee_email = invitee_email

    def __repr__(self):
        return "<Email user_id: {}, invitee_email: {}>".format(self.user_id, self.invitee_email)

    def to_dict(self):
        return dict(
            user_id=self.user_id,
            invitee_email=self.invitee_email,
        )

    @classmethod
    def from_dict(cls, dct):
        return cls(
            user_id=dct.get("user_id"),
            invitee_email=dct.get("invitee_email"),
        )
