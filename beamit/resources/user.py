from beamit.resources.base import Resource


class User(Resource):

    MEDIA_TYPE = 'application/vnd.beamit.user+json'

    def __init__(self, id, email, name=None, phone=None, company=None, linkedin_url=None):
        self.id = id
        self.email = email
        self.name = name
        self.phone = phone
        self.company = company
        self.linkedin_url = linkedin_url

    def __repr__(self):
        return "<User id: {}, email: {}, name: {}, phone: {},  company: {}, " \
            "linkedin_url: {}>".format(
                self.id,
                self.email,
                self.name,
                self.phone,
                self.company,
                self.linkedin_url,
            )

    def to_dict(self):
        return dict(
            id=self.id,
            email=self.email,
            name=self.name,
            phone=self.phone,
            company=self.company,
            linkedin_url=self.linkedin_url,
        )

    @classmethod
    def from_dict(cls, dct):
        return cls(
            id=dct.get("id"),
            email=dct.get("email"),
            name=dct.get("name"),
            phone=dct.get("phone"),
            company=dct.get("company"),
            linkedin_url=dct.get("linkedin_url"),
        )
