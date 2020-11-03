from requests import Response, post
import os
from typing import List


class MailgunException(Exception):
    def __init__(self, message: str):
        self.message = message


class Mailgun:
    FROM_TITLE = "Pricing Alert Service"
    FROM_EMAIL = "do-not-reply@sandboxea7f94db2e4c4b58ba2c8920609d4c4b.mailgun.org"

    @classmethod
    def send_mail(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        api_key = os.environ.get("MAILGUN_API_KEY", None)
        domain = os.environ.get("MAILGUN_DOMAIN", None)
        if api_key is None:
            raise MailgunException("Failed to get Mailgun API Key")
        if domain is None:
            raise MailgunException("Failed to get Mailgun Domain")
        response = post(
            f"{domain}/messages",
            auth=("api", f"{api_key}"),
            data={"from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                  "to": email,
                  "subject": subject,
                  "text": text,
                  "html": html})

        if response.status_code != 200:
            raise MailgunException("An error occurred while sending e-mail.")
        return response
