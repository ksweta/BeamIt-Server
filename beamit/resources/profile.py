from beamit.resources.base import Resource


class Profile(Resource):

    MEDIA_TYPE = 'application/vnd.beamit.profile+json'

    def __init__(self, user_id, name, phone, email, company, linkedin_url):
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.email = email
        self.company = company
        self.linkedin_url = linkedin_url

    def __repr__(self):
        return "<Profile user_id: {}, name: {}, phone: {}, email: {}, company: {}, " \
            "linkedin_url: {}>".format(
                self.user_id,
                self.name,
                self.phone,
                self.email,
                self.company,
                self.linkedin_url,
            )

    def to_dict(self):
        return dict(
            user_id=self.user_id,
            name=self.name,
            phone=self.phone,
            email=self.email,
            company=self.company,
            linkedin_url=self.linkedin_url,
        )

    @classmethod
    def from_dict(cls, dct):
        return cls(
            user_id=dct.get("user_id"),
            name=dct.get("name"),
            phone=dct.get("phone"),
            email=dct.get("email"),
            company=dct.get("company"),
            linkedin_url=dct.get("linkedin_url"),
        )
