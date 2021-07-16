from keystone import get_token
import json
import requests
from datetime import datetime
import os
def alertHandler(request):
    headers = {
     "X-Auth-Token": get_token(),
     "Content-Type": "application/json; charset=utf-8"
    }
    alerts = request.get("alerts", [])
    print(alerts)
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
         "event_id":  labels.get("event_id"),
         "data": {
            "instance": labels.get("instance", "")
          }
         }
      }
    
    orchestration_url = os.environ.get('orchestration_url', "http://127.0.0.1:9890")
    r = requests.post(orchestration_url + '/v1.0/alerts.json', data=json.dumps(data),headers=headers)
    
    return {}

