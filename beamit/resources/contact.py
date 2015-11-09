
from beamit.resources.base import Resource, PaginatedResourceList


class Contact(Resource):

    MEDIA_TYPE = 'application/vnd.beamit.contact+json'

    def __init__(self, id, owner_id, email, name=None, phone=None,  company=None, linkedin_url=None):  # noqa
        self.id = id
        self.owner_id = owner_id
        self.email = email
        self.name = name
        self.phone = phone
        self.company = company
        self.linkedin_url = linkedin_url

    def __repr__(self):
        return "<Contact id: {}, owner_id: {}, email: {}, name: {}, phone: {}, "\
            "company: {}, linkedin_url: {}>".format(
                self.id,
                self.owner_id,
                self.email,
                self.name,
                self.phone,
                self.company,
                self.linkedin_url,
            )

    def to_dict(self):
        return dict(
            id=self.id,
            owner_id=self.owner_id,
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
            owner_id=dct.get("owner_id"),
            email=dct.get("email"),
            name=dct.get("name"),
            phone=dct.get("phone"),
            company=dct.get("company"),
            linkedin_url=dct.get("linkedin_url"),
        )


class ContactList(PaginatedResourceList):
    """
    Contact list for a owner
    """
    MEDIA_TYPE = 'application/vnd.beamit.contact.list+json'

    @classmethod
    def items_name(cls):
        return "contacts"

    @classmethod
    def items_class(cls):
        return Contact
