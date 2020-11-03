import uuid
from typing import Dict
from models.model import Model
import re
from dataclasses import dataclass, field

@dataclass(eq=False)
class Store(Model):
    collection = "stores"
    collection: str = field(init=False, default="stores")
    name: str
    url_prefix: str
    tag_name: str
    query: dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    @classmethod
    def get_by_name(cls, store_name) -> "Store":
        return cls.find_one_by("name", store_name)

    @classmethod
    def get_by_url_prefix(cls, url_prefix: str) -> "Store":
        url_regex = {"$regex": "^{}".format(url_prefix)}
        return cls.find_one_by("url_prefix", url_regex)


    @classmethod
    def find_by_url(cls, url: str) -> "Store":
        pattern = re.compile(r"(https?://.*?/)")
#       https://www.unico-fan.co.jp/shop/g/gU53510143000000Z0022/
        match = pattern.search(url)
        url_prefix = match.group(1)
        return cls.get_by_url_prefix(url_prefix)






