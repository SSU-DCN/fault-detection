import yaml

class Alert():
  def __init__(self, file_content):
    data = yaml.safe_load(file_content)
    self._content = data.get("groups", [])
  def add_new_rule(self, alerts):
    alerts_obj = {}

    for alert in alerts:
      if not (alerts_obj.get(alert.group)):
        alerts_obj[alert.group] = []

      labels = dict(alert.labels)
      #labels = [{key: labels[key]} for key in dict.keys(labels)]

      annotations = dict(alert.annotations)
      #annotations = [{key: annotations[key]} for key in dict.keys(annotations)]

      new_rule = {
        "alert": alert.alert,
        "expr": alert.expr,
        "for": alert.duration,
        "labels": labels,
        "annotations": annotations
      }
      alerts_obj[alert.group].append(new_rule)

    for alert in self._content:
      if alerts_obj.get(alert.get("group")):
        alert.get("rules", []).append(alerts_obj[alert.get("group")])
        del alerts_obj[alert.get("group")]

    for key in alerts_obj:
      alerts = {
        "name": key,
        "rules": alerts_obj[key]
      }
      self._content.append(alerts)
  def __repr__(self):
    try:
      add_to_group = {"group": self._content}
      return yaml.dump(add_to_group)
    except:
      raise
