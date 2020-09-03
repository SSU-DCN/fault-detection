import yaml
import io
import os
import json

class AlertRule:
    def __init__(self, _metric_type, expresstion, threshold_value, operator, action):
        self._metric_type = _metric_type
        self._expresstion = expresstion
        self._threshold_value = str(threshold_value)
        self._operator = operator
        self._action = action
    
    def _find_action_index(self, groups):
        for i in range(len(groups)):
            if groups[i]["name"] == self._action:
                return i
        return -1

    def _generate_new_rule(self):
        rule = {
            "alert": self._metric_type,
            "expr": self._expresstion + self._operator + self._threshold_value,
            "for": "30s"
        }

        return rule

    def export_to_file(self, file_name):
        data = None
        if os.path.exists(file_name):
            with open(file_name) as data_file:
                data =  yaml.full_load(data_file)

        groups = data.get("groups") if data else []
        action_index = self._find_action_index(groups)

        if action_index > -1:
            groups[action_index]["rules"].append(self._generate_new_rule())
        else:
            groups.append({
                "name": self._action,
                "rules": [self._generate_new_rule()]
            })

        export_data = { "groups": groups}
        with open(file_name, '+w') as file:
            yaml.dump(export_data, file)
