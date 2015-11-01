from beamit.app import db
from beamit.resources.contact import Contact as ContactResource


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    email = db.Column(db.String(60), unique=True, nullable=False)
    name = db.Column(db.String(64))
    phone = db.Column(db.String(15))
    company = db.Column(db.String(50))
    linkedin_url = db.Column(db.String(100))
    photo = db.Column(db.LargeBinary)

    def __init__(self, owner_id, email, name=None, phone=None, company=None, linkedin_url=None, photo=None):  # noqa
        self.owner_id = owner_id
        self.email = email
        self.name = name
        self.phone = phone
        self.company = company
        self.linkedin_url = linkedin_url
        self.photo = photo

    def __repr__(self):
        return "<Contact id: {}, owner_id: {}, email: {}, name: {}, phone: {}, "\
            "company: {}, linkedin_url: {}, photo_present: {}>".format(
                self.id,
                self.owner_id,
                self.email,
                self.name,
                self.phone,
                self.company,
                self.linkedin_url,
                True if self.photo else False,
            )

    def to_contact_resource(self):
        """
        This method converts `beamit.resources.contact.Contact` object to model object
        """
        return ContactResource(
            id=self.id,
            owner_id=self.owner_id,
            email=self.email,
            name=self.name,
            phone=self.phone,
            company=self.company,
            linkedin_url=self.linkedin_url,
        )

    @classmethod
    def from_contact_resource(cls, resource):
        return cls(
            owner_id=resource.owner_id,
            email=resource.email,
            name=resource.name,
            phone=resource.phone,
            company=resource.company,
            linkedin_url=resource.linkedin_url,
        )
