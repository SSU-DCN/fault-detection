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
        "vdu_name": vnf_id + "_" + vdu.vdu_name,
        'vnf_id': vnf_id
      },
      "targets": [vdu.mgmt_ip + ':' + vdu.exporter_port]
    }
    self._content.append(new_target)

  def del_target(self, vnf_id):
    result = []
    for i in self._content:
      if i['labels']['vnf_id'] != vnf_id:
        result.append(i)
    self._content = result
  def __repr__(self):
    return json.dumps(self._content,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
