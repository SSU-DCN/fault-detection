from keystone import get_token
import json
import requests


def alertHandler(request):
    headers = {
     "X-Auth-Token": get_token(),
     "Content-Type": "application/json; charset=utf-8"
    }

    alerts = request.get("alerts", [])
    for alert in alerts:
      labels = alert.get("labels", {})
      data = {
        "alert": {
          "event_id": labels.get("event_id")
        }
      }

    r = requests.post('http://127.0.0.1:9890/v1.0/alerts.json', data=json.dumps(data),headers=headers)
    
    return {}

