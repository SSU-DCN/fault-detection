import service_pb2
import service_pb2_grpc
from filesd import FileSD
from file_manipulation import File
from alert import Alert
import sys, traceback
import requests
import os

class MonitorServicer(service_pb2_grpc.MonitorServicer):
  def __init__(self, target_file, alert_file):
    self._target_file = target_file
    self._alert_file = alert_file
  def NewTargetRequest(self, request, context):
    try:
      target_file = File(self._target_file)
      target_file_content = target_file.open_file()
      fild_sd = FileSD(target_file_content)

      alert_file = File(self._alert_file)
      alert_file_content = alert_file.open_file()
      alerts = Alert(alert_file_content)

      for vdu in request.vdus:
        fild_sd.add_new_target(vdu, request.vnf_id)
        alerts.add_new_rule(alerts=vdu.alerts, vnf_id=request.vnf_id, vdu_name=vdu.vdu_name)
      
      target_file.write_to_file(str(fild_sd))
      alert_file.write_to_file(str(alerts))
      
      # Reload prometheus configuration
      r = requests.post(os.environ['prometheus_api_server'] + "/-/reload")
      print("New target created")
      response = service_pb2.MonitorReply(message = "", status =1)
      return response
    except:
      traceback.print_exc(file=sys.stdout)
      response = service_pb2.MonitorReply(message = "Unexpected error:", status =1) 
      return response
  def DelTargetRequest(self, request, context):
    try:
      target_file = File(self._target_file)
      target_file_content = target_file.open_file()
      fild_sd = FileSD(target_file_content)

      alert_file = File(self._alert_file)
      alert_file_content = alert_file.open_file()
      alerts = Alert(alert_file_content)

      fild_sd.del_target(vnf_id = request.vnf_id)
      target_file.write_to_file(str(fild_sd))

      alerts.delete_rule(vnf_id = request.vnf_id)
      alert_file.write_to_file(str(alerts))

      response = service_pb2.MonitorReply(message = "", status =1)
      r = requests.post(os.environ['prometheus_api_server']+ "/-/reload")
      print("Target deleted")

      return response
    except:
      traceback.print_exc(file=sys.stdout)
      response = service_pb2.MonitorReply(message = "Unexpected error:", status =1) 
      return response
