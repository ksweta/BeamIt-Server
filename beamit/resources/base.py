from abc import ABCMeta, abstractmethod, abstractproperty


class Resource(object):
    __metaclass__ = ABCMeta

    # TODO:
    #  - automate to_dict() and from_dict() based on members
    #  - automate camelCase and snake_case conversions
    #  - automate type conversions

    @classmethod
    def media_type(cls):
        return cls.MEDIA_TYPE

    def _dict_no_none(self, **kwargs):
        return {
            k: v
            for k, v in kwargs.iteritems()
            if v is not None
        }

    @abstractmethod
    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, resource_dict):
        raise NotImplementedError()

    def __hash__(self):
        return hash(frozenset(self.to_dict()))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.to_dict() == other.to_dict()

    def __ne__(self, other):
        return self.to_dict() != other.to_dict()


class ResourceList(Resource):

    @abstractproperty
    def resources(self):
        pass

    def __len__(self):
        return len(self.resources)

    def __iter__(self):
        return iter(self.resources)

    def append(self, resource):
        self.resources.append(resource)
