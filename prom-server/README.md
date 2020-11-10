## Prometheus's GRPC server
This repo is the GRPC server to add monitor target to Prometheus's service 
discovery file and add alert rule. This allows others components to send monitor
request to Prometheus without accessing to the server

## Start commands
```
python3 server.py  --filesd targets.json --alertfile alert-rule.yml
--filesd: The location of file-servicediscovery that is listed in the Prometheus configuration
--alert-file: The location of alert rule file that is listed in the Prometheus configuration
```
## Generate Python's proto file
```
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto 
```
