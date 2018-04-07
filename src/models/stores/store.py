import uuid
import src.models.stores.constants as StoreConstants
from src.common.database import Database
import src.models.stores.errors  as StoreErrors

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
    def get_by_id(cls,id):
        return cls(**Database.find_one(StoreConstants.CONSTANT,{'_id':id}))

    @classmethod
    def get_by_name(cls,name):
        return cls(**Database.find_one(StoreConstants.CONSTANT, {'name': name}))

    @classmethod
    def get_by_url_prefix(cls,url_prefix):
        return cls(**Database.find_one(StoreConstants.CONSTANT,{'url_prefix':{"$regex":"^{}".format(url_prefix)}}))

    def save_to_mongo(self):
        Database.insert(StoreConstants.CONSTANT,self.json())

    @classmethod
    def find_by_url(cls,url):

        for i in range(len(url)):
            try:
                store = Store.get_by_url_prefix(url[:i])
                return store
            except:
                raise StoreErrors.StoreNotFoundException("The URL prefix used to find the URL doesn't give ant URL")