import json

class FileSD():
  def __init__(self, file_content):
    try:
      data = json.loads(file_content)
    except:
      data = []
    self._content = data
  def add_new_target(self, vdu):
    new_target = {
      "labels": {
        "vnf_name": vdu.vnf_name
      },
      "target": vdu.mgmt_ip
    }
    self._content.append(new_target)
  def __repr__(self):
    return json.dumps(self._content,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
