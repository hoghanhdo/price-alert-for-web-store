import uuid
from typing import Dict, List

from common.database import Database
from models.item import Item
from models.model import Model


class Alert(Model):
    collection = "alerts"

    def __init__(self, item_id: str, price_limit: int, _id: str = None):
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self._id = _id or uuid.uuid4().hex

    def json(self):
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "item_id": self.item_id
        }

    def save_to_mongo(self):
        Database.insert(self.collection, self.json())

    def load_item_price(self):
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print(f"Item {self.item} has reached a price under ¥{self.price_limit}\nLatest price: ¥{self.item.price}")
        else:
            print(f"There is no change in the price of Item {self.item}\nCurrent price is ¥{self.item.price}")

    @classmethod
    def get_by_id(cls, _id):
        return cls(**Database.find_one(cls.collection, query={"_id": _id}))

    @classmethod
    def all(cls):
        alerts_from_db = Database.find(cls.collection, {})
        return [cls(**alert) for alert in alerts_from_db]
