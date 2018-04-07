import uuid
import src.models.stores.constants as StoreConstants
from src.common.database import Database


class Store(object):
    def __init__(self, name, url_prefix,tag_name,query,_id=None):
        self.name = name
        self.prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Store {}>".format(self.name)

    def json(self):
        return {
            "_id":self._id,
            "name":self.name,
            "url_prefix":self.prefix,
            "tag_name":self.tag_name,
            "query":self.query
        }

    @classmethod
    def get_from_id(cls,id):
        return cls(**Database.find_one(StoreConstants.CONSTANT,{'_id':id}))


