from beamit.resources.base import Resource


class SignupRequest(Resource):
    MEDIA_TYPE = 'application/vnd.beamit.signup.request+json'

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return "<SignupRequest email: {}, password: {}>".format(
            self.email,
            self.password,
        )

    def to_dict(self):
        return dict(email=self.email, password=self.password)

    @classmethod
    def from_dict(cls, dct):
        return cls(
            email=dct.get("email"),
            password=dct.get("password"),
        )


class SignupResponse(Resource):

    MEDIA_TYPE = 'application/vnd.beamit.signup.response+json'

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "<SignupResponse user_id: {}>".format(self.user_id)

    def to_dict(self):
        return dict(user_id=self.user_id)

    @classmethod
    def from_dict(cls, dct):
        return cls(user_id=dct.get("user_id"))
