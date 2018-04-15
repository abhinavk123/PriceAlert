import uuid

import datetime

import src.models.alerts.constants as AlertConstants
import requests

from src.common.database import Database
from src.models.items.item import Item


class Alert(object):
    def __init__(self, user_email, price_limit, item_id, last_checked=None, _id=None, active=True):
        self.user_email = user_email
        self.price_limit = price_limit
        self.item = Item.get_by_id(item_id)
        self.last_checked = datetime.datetime.utcnow() if last_checked is None else last_checked
        self._id = uuid.uuid4().hex if _id is None else _id
        self.active = active

    def __repr__(self):
        return "<Alert for {} on item {} with price {}>".format(self.user_email, self.item, self.price_limit)

    def send(self):
        return requests.post(
            AlertConstants.URL,
            auth=("api", AlertConstants.APIKEY),
            data={
                "from": AlertConstants.FROM,
                "to": [self.user_email],
                "subject": "Price Limit reached for {}".format(self.item.name),
                "text": "We've found a deal! ({}).".format(self.item.url)
            }

        )

    @classmethod
    def find_needing_update(cls, minutes_since_update=AlertConstants.ALERT_TIMEOUT):
        last_update_limit = datetime.datetime.utcnow() - datetime.timedelta(minutes=minutes_since_update)
        return [cls(**elm) for elm in
                Database.find(AlertConstants.COLLECTION, {"last_checked": {"$lte": last_update_limit}, 'active': True})]

    def save_to_mongo(self):
        Database.update(AlertConstants.COLLECTION, {'_id': self._id}, self.json())

    def json(self):
        return {
            '_id': self._id,
            'user_email': self.user_email,
            'price_limit': self.price_limit,
            'last_checked': self.last_checked,
            'item_id': self.item._id,
            'active': self.active

        }

    def load_item_price(self):
        self.item.load_price()
        self.last_checked = datetime.datetime.utcnow()
        self.save_to_mongo()
        self.item.save_to_mongo()
        return self.item.price

    def send_email_if_price_reached(self):
        if self.item.price < self.price_limit:
            print(self.send())

    def deactivate(self):
        self.active = False
        self.save_to_mongo()

    def activate(self):
        self.active = True
        self.save_to_mongo()

    def delete(self):
        Database.remove(AlertConstants.COLLECTION, {'_id': self._id})

    @classmethod
    def find_by_email(cls, user_email):
        return [cls(**alt) for alt in Database.find(AlertConstants.COLLECTION, {'user_email': user_email})]

    @classmethod
    def find_by_id(cls, alert_id):
        return cls(**Database.find_one(AlertConstants.COLLECTION, {'_id': alert_id}))
