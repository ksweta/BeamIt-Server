from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from beamit.app import db
from beamit.resources.user import User as UserResource


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(160), nullable=False)
    name = db.Column(db.String(64))
    phone = db.Column(db.String(15))
    company = db.Column(db.String(50))
    linkedin_url = db.Column(db.String(100))
    photo = db.Column(db.LargeBinary)
    contacts = db.relationship('Contact', backref="owner", lazy='dynamic')

    def __init__(self, email, password,  name=None, phone=None, company=None, linkedin_url=None, photo=None):  # noqa
        self.email = email
        # Generate the one way hash password
        self.set_password(password)
        self.name = name
        self.phone = phone
        self.company = company
        self.linkedin_url = linkedin_url
        self.photo = photo

    def __repr__(self):
        return "<User id: {}, email: {}, password: {}, name: {}, phone: {}, company: {}, " \
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

    def set_password(self, password):
        """
        This method generates one way hash of the password
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        This method generates one way hash of the given password and compares it with the stored
        password
        """
        return check_password_hash(self.password, password)

    def to_user_resource(self):
        return UserResource(
            id=self.id,
            email=self.email,
            password=self.password,
            name=self.name,
            phone=self.phone,
            company=self.company,
            linkedin_url=self.linkedin_url,
        )

    @classmethod
    def from_user_resource(cls, resource):
        return cls(
            email=resource.email,
            password=resource.password,
            name=resource.name,
            phone=resource.phone,
            company=resource.company,
            linkedin_url=resource.linkedin_url,
        )
