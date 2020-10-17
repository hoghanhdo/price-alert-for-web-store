from models.item import Item
from models.alert import Alert

item = Item(
    url="https://www.unico-fan.co.jp/shop/g/gU53650103000000Z0134/",
    tag_name="p",
    query={"class": "net_sale"}
)

item.save_to_mongo()
alert = Alert(item._id, 5000)
alert.save_to_mongo()