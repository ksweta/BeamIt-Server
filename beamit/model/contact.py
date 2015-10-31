from beamit.app import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    email = db.Column(db.String(60), unique=True, nullable=False)
    name = db.Column(db.String(64))
    phone = db.Column(db.String(15))
    company = db.Column(db.String(50))
    linkedin_url = db.Column(db.String(100))

    def __init__(self, owner_id, email, name, phone=None, company=None, linkedin_url=None):
        self.owner_id = owner_id
        self.email = email
        self.name = name
        self.phone = phone
        self.company = company
        self.linkedin_url = linkedin_url

    def __repr__(self):
        return "<Contact id: {}, owner_id: {}, name: {}, email: {}, phone: {}, "\
            "company: {}, linkedin_url: {}>".format(
                self.id,
                self.owner_id,
                self.name,
                self.email,
                self.phone,
                self.company,
                self.linkedin_url,
            )
