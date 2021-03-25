from keystone import get_token
import json
import requests


def alertHandler(request):
    headers = {
     "X-Auth-Token": get_token(),
     "Content-Type": "application/json; charset=utf-8"
    }
    alerts = request.get("alerts", [])
    if len(alerts):
     for alert in alerts:
       labels = alert.get("labels", {})
       print(alert, labels)
       data = {
         "alert": {
           "event_id": labels.get("event_id")
         }
       }
    else:
     labels = request.get("labels", {})   
     data = { 
      "alert": {
         "event_id":  labels.get("event_id")
         }
       }

    data['alert']['data'] = {}
    data['alert']['data']['body'] =  {
        "name": "test1",
        "replicas": 1,
        "action":"live-migration",
        "sourcePod":"nginx-migration-16",
        "destHost":"worker2"
    }
    r = requests.post('http://127.0.0.1:9890/v1.0/alerts.json', data=json.dumps(data),headers=headers)
    
    return {}

