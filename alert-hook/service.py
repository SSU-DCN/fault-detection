from keystone import get_token
import json
import requests
from datetime import datetime

def alertHandler(request):
    headers = {
     "X-Auth-Token": get_token(),
     "Content-Type": "application/json; charset=utf-8"
    }
    alerts = request.get("alerts", [])
    if len(alerts):
     for alert in alerts:
       labels = alert.get("labels", {})
       data = {
         "alert": {
           "event_id": labels.get("event_id"),
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
    data['alert']['data']['instance'] = '192.168.5.192'
    data['alert']['data']['body'] =  {
        "name": "test" + str(datetime.now().timestamp()),
        "replicas": 1,
        "action":"live-migration",
        "sourcePod":"video",
        "destHost":"worker1"
    }
    r = requests.post('http://127.0.0.1:9890/v1.0/alerts.json', data=json.dumps(data),headers=headers)
    
    return {}

