from beamit.app import db
from beamit.resources.profile import Profile as ProfileResource


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(64))
    phone = db.Column(db.String(15))
    company = db.Column(db.String(50))
    linkedin_url = db.Column(db.String(100))
    photo = db.Column(db.LargeBinary)
    contacts = db.relationship('Contact', backref="owner", lazy='dynamic')

    def __init__(self, email, password,  name=None, phone=None, company=None, linkedin_url=None, photo=None):  # noqa
        self.email = email
        self.password = password
        self.name = name
        self.phone = phone
        self.company = company
        self.linkedin_url = linkedin_url
        self.photo = photo

    def __repr__(self):
        return "<Profile id: {}, email: {}, password: {}, name: {}, phone: {}, company: {}, " \
            "linkedin_url: {}, photo_present: {}>".format(
                self.id,
                self.email,
                self.password,
                self.name,
                self.phone,
                self.company,
                self.linkedin_url,
                True if self.photo else False,
            )

    def to_profile_resource(self):
        return ProfileResource(
            id=self.id,
            email=self.email,
            password=self.password,
            name=self.name,
            phone=self.phone,
            company=self.company,
            linkedin_url=self.linkedin_url,
        )

    @classmethod
    def from_profile_resource(cls, resource):
        return cls(
            email=resource.email,
            password=resource.password,
            name=resource.name,
            phone=resource.phone,
            company=resource.company,
            linkedin_url=resource.linkedin_url,
        )
