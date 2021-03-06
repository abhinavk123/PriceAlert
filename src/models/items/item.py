import re
import uuid
import src.models.items.constants as ItemConstants
import requests
from bs4 import BeautifulSoup
from src.common.database import Database
from src.models.stores.store import Store


class Item(object):
    def __init__(self,name,url,price=None,_id = None):
        self.name = name
        self.url = url
        store = Store.find_by_url(url)
        self.tag_name = store.tag_name
        self.query = store.query
        self.price = None if price is  None  else price
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Item {} with URL {}".format(self.name,self.url)

    def load_price(self):
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content,"html.parser")
        element = soup.find(self.tag_name,self.query)
        el = element.text.split('\n')
        string_price = el[4]
        self.name=el[1]
        #pattern = re.compile("(\d+.\d+)")
        #match = pattern.search(string_price)

        #return match.group()

        self.price = float(string_price[1:])

        return float(string_price[1:])

    def save_to_mongo(self):
        Database.update(ItemConstants.COLLECTION,{'_id':self._id},self.json())

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
            'url':self.url,
            'price':self.price
        }
