import os

ADMIN = os.environ.get("ADMIN")
MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")
FROM_EMAIL = os.environ.get("FROM_EMAIL")
MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN")
ALERT_TIMEOUT = 10
COLLECTIONS = "alerts"
