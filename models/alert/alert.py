import uuid
from dataclasses import dataclass, field
from models.item import Item
from models.model import Model
from models.user import User


@dataclass(eq=False)
class Alert(Model):
    name: str
    item_id: str
    price_limit: int
    user_email: str
    collection: str = field(init=False, default="alerts")
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __post_init__(self):
        self.item = Item.get_by_id(self.item_id)
        self.user = User.find_by_email(self.user_email)

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "price_limit": self.price_limit,
            "item_id": self.item_id,
            "user_email": self.user_email
        }

    def load_item_price(self):
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print(f"Item {self.item} has reached a price under ¥{self.price_limit}\nLatest price: ¥{self.item.price}")
        else:
            print(f"There is no change in the price of Item {self.item}\nCurrent price is ¥{self.item.price}")

