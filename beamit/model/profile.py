from beamit.app import db


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(15))
    company = db.Column(db.String(50))
    linkedin_url = db.Column(db.String(100))
    photo = db.Column(db.LargeBinary)
    contacts = db.relationship('Contact', backref="owner", lazy='dynamic')

    def __init__(self, name, email, password, phone=None, company=None, linkedin_url=None, photo=None):  # noqa
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.company = company
        self.linkedin_url = linkedin_url
        self.photo = photo

    def __repr__(self):
        return "<Profile id: {}, name: {}, email: {}, password: {}, phone: {}, company: {}, " \
            "linkedin_url: {}, photo_present: {}>".format(
                self.id,
                self.name,
                self.email,
                self.password,
                self.phone,
                self.company,
                self.linkedin_url,
                True if self.photo else False,
            )
