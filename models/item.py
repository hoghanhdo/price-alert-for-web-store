import re
import uuid

import requests
from bs4 import BeautifulSoup
from typing import Dict

from common.database import Database
from models.model import Model


class Item(Model):
    collection = "items"

    def __init__(self, url: str, tag_name: str, query: dict, _id: str = None):
        super().__init__()
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None
        self._id = _id or uuid.uuid4().hex

    def __repr__(self):
        return f"<Item {self.url}>"

    def json(self):
        return {
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "query": self.query
        }

    # def save_to_mongo(self):
    #     Database.insert(self.collection, self.json())

    def load_price(self):
        content = requests.get(self.url).content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        priceStr = element.text.strip()

        pattern = re.compile(r"(\d+,\d+)")
        match = pattern.search(priceStr)
        priceStr = match.group(1)
        priceStr_without_comma = priceStr.replace(",", "")
        self.price = int(priceStr_without_comma)
        return self.price

    # @classmethod
    # def all(cls):
    #     items_from_db = Database.find(cls.collection, query={})
    #     return [cls(**item) for item in items_from_db]

    # @classmethod
    # def get_by_id(cls, _id):
    #     item_json = Database.find_one(cls.collection, query={"_id": _id})
    #     return cls(**item_json)
