import re
import uuid

import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass, field
from models.model import Model
from typing import Dict


@dataclass(eq=False)
class Item(Model):
    collection: str = field(init=False, default="items")
    url: str
    tag_name: str
    query: dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
    price: int = field(default=None)

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "price": self.price,
            "query": self.query
        }

    def load_price(self) -> int:
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        pattern = re.compile(r"(\d+,\d+)")
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(",", "")
        self.price = int(without_commas)
        return self.price


