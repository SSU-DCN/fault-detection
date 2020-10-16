import json

class FileSD():
  def __init__(self, file_content):
    try:
      data = json.loads(file_content)
    except:
      data = []
    self._content = data
  def add_new_target(self, vdu, vnf_id):
    new_target = {
      "labels": {
        "vdu_name": vdu.vdu_name,
        'vnf_id': vnf_id
      },
      "targets": [vdu.mgmt_ip + ':' + vdu.exporter_port]
    }
    self._content.append(new_target)

  def del_target(self, vnf_id):
    for i in range(len(self._content)):
      target = self._content[i]
      if target['labels']['vnf_id'] == vnf_id:
        self._content.pop(i)

  def __repr__(self):
    return json.dumps(self._content,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
