import requests


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxea7f94db2e4c4b58ba2c8920609d4c4b.mailgun.org/messages",
        auth=("api", "4d42d574da4a77a97402111a032e6d9f-ea44b6dc-fdc4f782"),
        data={"from": "Pricing Alert Service <do-not-reply@sandboxea7f94db2e4c4b58ba2c8920609d4c4b.mailgun.org>",
              "to": ["hoghanhdo@gmail.com", "hoghanhdo@outlook.com"],
              "subject": "Pricing Alert",
              "text": "Welcome to Mailgun"})


print(send_simple_message())
