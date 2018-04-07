import re
import uuid
import src.models.users.constants as ItemConstants
import requests
from bs4 import BeautifulSoup
from src.common.database import Database
from src.models.stores.store import Store


class Item(object):
    def __init__(self,name,url,_id = None):
        self.name = name
        self.url = url
        store = Store.find_by_url(url)
        tag_name = store.tag_name
        query = store.query
        self.price = self.load_price(tag_name,query)
        self._id = uuid.uuid4().hex if _id is None else _id


    def __repr__(self):
        return "<Item {} with URL {}".format(self.name,self.url)


    def load_price(self,tag_name,query):
        request = requests.get(self.url)
        content = request.content

        soup = BeautifulSoup(content,"html.parser")

        element = soup.find(tag_name,query)

        string_price = element.text.strip()

        #pattern = re.compile("(\d+.\d+)")
        #match = pattern.search(string_price)

        #return match.group()

        return string_price[1:]

    def save_to_mongo(self):
        Database.insert(ItemConstants.COLLECTION,self.json())

    @classmethod
    def get_by_id(cls,id):
        item = Database.find_one(ItemConstants.COLLECTION,{'_id':id})
        if item is not None:
            return cls(**item)
        else:
            return "No Item Found"

    def json(self):
        return {
            '_id':self._id,
            'name':self.name,
            'url':self.url
        }
