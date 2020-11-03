from flask import Flask, render_template
from views.alert import alert_blueprint
from views.store import store_blueprint
from views.user import user_blueprint
import os

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)


@app.route('/')
def index():
    return render_template("index.html")


app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(user_blueprint, url_prefix="/users")

if __name__ == "__main__":
    app.run(debug=True)
