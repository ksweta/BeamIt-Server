from beamit.resources.base import Resource


class PasswordChangeRequest(Resource):

    MEDIA_TYPE = 'application/vnd.beamit.password.change.request+json'

    def __init__(self, email, password, new_password):
        self.email = email
        self.password = self.password
        self.new_password = new_password

    def __repr__(self):
        return "<PasswordChangeRequest email: {}, password: {}, new_password: {}>".format(
            self.email,
            self.password,
            self.new_password,
        )

    def to_dict(self):
        return dict(email=self.email, password=self.password, new_password=self.new_password)

    @classmethod
    def from_dict(cls, dct):
        return cls(
            email=dct.get("email"),
            password=dct.get("password"),
            new_password=dct.get("new_password"),
        )


class PasswordChangeResponse(Resource):

    MEDIA_TYPE = 'application/vnd.beamit.password.change.response+json'

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "<PasswordChangeResponse user_id: {}>".format(self.user_id)

    def to_dict(self):
        return dict(user_id=self.user_id)

    @classmethod
    def from_dict(cls, dct):
        return cls(user_id=dct.get("user_id"))
