import grpc

# import the generated classes
import service_pb2
import service_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = service_pb2_grpc.MonitorStub(channel)

# create a valid request message
group = "alert"
alert = "high_cpu"
expr = "x>y"
duration = "5m"
labels = {
  "severity": "page",
  "vnf_name": "pageee",
}
annotations= {
  "summary": "High request latency"
}

first_alert = service_pb2.Alert(
  group = group, alert = alert, expr = expr, duration= duration,
  labels= labels, annotations=annotations
)

vnf_name = "test"
mgmt_ip = "192.168.1.1"
alerts = [first_alert]
vdus = service_pb2.Vdu(vnf_name= vnf_name, mgmt_ip = mgmt_ip, alerts = alerts)

vnf_id = "abc"
monitor_request = service_pb2.MonitorRequest(vnf_id=vnf_id, vdus= [vdus])

# make the call
response = stub.NewTargetRequest(monitor_request)

# et voilà
print(response)
