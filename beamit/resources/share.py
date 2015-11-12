"""
Share resource
"""
from beamit.resources.base import Resource


class Share(Resource):

    MEDIA_TYPE = 'application/vnd.beamit.share+json'

    def __init__(self, owner_id, subject_id):
        """
        :param owner_id: who receives the contact information.
        :param subject_id: Who shares the contact information.
        """
        self.owner_id = owner_id
        self.subject_id = subject_id

    def __repr__(self):
        return "<Share owner_id: {}, subject_id: {}>".format(self.owner_id, self.subject_id)

    def to_dict(self):
        return dict(owner_id=self.owner_id, subject_id=self.subject_id)

    @classmethod
    def from_dict(cls, dct):
        return cls(
            owner_id=dct.get("owner_id"),
            subject_id=dct.get("subject_id"),
        )
