import yaml

class Alert():
  def __init__(self, file_content):
    data = yaml.safe_load(file_content)
    self._content = data.get("groups", [])
  def add_new_rule(self, alerts, vnf_id, vdu_name):
    alerts_obj = {}
    for alert in alerts:
      if not (alerts_obj.get(alert.group)):
        alerts_obj[alert.group] = []
      new_rule = {
        "alert": alert.alert + "_" + vnf_id + "_" + vdu_name,
        "expr": alert.expr,
        "for": alert.duration,
        "labels": dict(alert.labels),
        "annotations": dict(alert.annotations)
      }
      alerts_obj[alert.group].append(new_rule)

    for alert in self._content:
      if alerts_obj.get(alert.get("name")):
        alert.get("rules", []).extend(alerts_obj[alert.get("name")])
        del alerts_obj[alert.get("name")]

    for key in alerts_obj:
      alerts = {
        "name": key,
        "rules": alerts_obj[key]
      }
      self._content.append(alerts)
  def delete_rule(self, vnf_id):
    result = []
    for group in self._content:
      new_rule = []
      rules = group.get("rules", [])
      for rule in rules:
        if vnf_id not in rule.get("alert"):
          new_rule.append(rule)
      if len(new_rule):
        alerts = {
          "name": group.get("name"),
          "rules": new_rule
        }
        result.append(alerts)
    self._content = result
  def __repr__(self):
    try:
      add_to_group = {"groups": self._content}
      return yaml.dump(add_to_group)
    except:
      raise
