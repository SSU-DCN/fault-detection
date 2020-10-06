from concurrent import futures
import time
import grpc
import service_pb2_grpc
import argparse
import os
from file_manipulation import File
from monitor_servicer import MonitorServicer


_MIN_IN_SECONDS = 60
_ONE_DAY_IN_SECONDS = _MIN_IN_SECONDS * _MIN_IN_SECONDS * 24


def check_if_file(file_dir):
  file_to_check = File(file_dir)
  return file_to_check.is_file()

def serve(target_file, alert_file):
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  service_pb2_grpc.add_MonitorServicer_to_server(MonitorServicer(target_file= target_file, alert_file=alert_file), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  print("Server started")
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
      server.stop(0)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Grpc server to add Prometheus's new monitor target")
  parser.add_argument('--filesd', required=True, help='Prometheus file-SD directory')
  parser.add_argument('--alertfile', required=True, help='Alert rule file')
  args = parser.parse_args()
  if not check_if_file(args.filesd) or not check_if_file(args.alertfile): 
    print(args.__dict__)
    raise TypeError("Can't not found target file")

  serve(target_file = args.filesd, alert_file= args.alertfile)