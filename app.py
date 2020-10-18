from flask import Flask
from views.item import item_blueprint
from views.alert import alert_blueprint

app = Flask(__name__)

app.register_blueprint(item_blueprint, url_prefix="/items")
app.register_blueprint(alert_blueprint, url_prefix="/alerts")


if __name__ == "__main__":
    app.run(debug=True)
