import requests
from config import ELASTIC_EMAIL


def send(to, subject, body, attachments):
    data = {
        "apikey": ELASTIC_EMAIL["APIKEY"],
        "subject": subject,
        "from": ELASTIC_EMAIL["FROM"],
        "fromName": ELASTIC_EMAIL["FROM_NAME"],
        "to": to,
        "bodyHtml": body,
        "isTransactional": False
    }
    attachments = attachments if type(attachments) == list else [attachments]
    attachs = [(name, open(name, "rb")) for name in attachments]
    result = requests.post(
        ELASTIC_EMAIL["URL"],
        params=data,
        files=attachs
    )
    result_json = result.json()
    if not result_json["success"]:
        return False, result_json["error"]
    return True, result_json["data"]
