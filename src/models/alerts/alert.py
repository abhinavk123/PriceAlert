import uuid

import datetime

import src.models.alerts.constants as AlertConstants
import requests

from src.common.database import Database


class Alert(object):
    def __init__(self,user,price_limit,item,last_checked=None,_id=None):
        self.user = user
        self.price_limit = price_limit
        self.item = item
        self.last_checked = datetime.datetime.utcnow() if last_checked is None else last_checked
        self._id = uuid.uuid4().hex if _id is None else _id
    def __repr__(self):
        return "<Alert for {} on item {} with price {}>".format(self.user.email,self.item,self.price_limit)

    def send(self):
        return requests.post(
            AlertConstants.URL,
            auth=("api",AlertConstants.APIKEY),
            data={
                "from":AlertConstants.FROM,
                "to":self.user.email,
                "subject":"Price Limit reached for {}".format(self.item.name),
                "text":"We've found a deal! (link  here)."
            }

        )

    @classmethod
    def find_needing_update(cls,minutes_since_update = AlertConstants.ALERT_TIMEOUT):
        last_update_limit = datetime.datetime.utcnow()-datetime.timedelta(minutes=minutes_since_update)
        return [cls(**elm) for elm in Database.find(AlertConstants.COLLECTION,{"last_checked":{"$gte":last_update_limit}})]