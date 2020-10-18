from flask import render_template, request, Blueprint
from models.alert import Alert
import json

alert_blueprint = Blueprint("alerts", __name__)


@alert_blueprint.route("/")
def index():
    alerts = Alert.all()
    return render_template("alerts/index.html", alerts=alerts)


@alert_blueprint.route("/new", methods=["GET", "POST"])
def new_alert():
    if request.method == "POST":
        item_id = request.form["item_id"]
        price_limit = request.form["price_limit"]

        Alert(item_id=item_id, price_limit=price_limit).save_to_mongo()
    return render_template("alerts/new_alert.html")
