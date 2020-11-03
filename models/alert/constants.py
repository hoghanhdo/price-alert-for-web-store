import os

ADMIN = os.environ.get("ADMIN")
MAILGUN_URL = os.environ.get("MAILGUN_URL")
API_KEY = os.environ.get("API_KEY")
FROM_EMAIL = os.environ.get("FROM_EMAIL")
DOMAIN = os.environ.get("DOMAIN")
ALERT_TIMEOUT = 10
COLLECTIONS = "alerts"
