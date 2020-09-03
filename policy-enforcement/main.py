import yaml
from fileSD import FileSD
from alertRule import AlertRule
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Policy enforcement based on policy template ')
    parser.add_argument('--template', required=True, help='Template directory')
    parser.add_argument('--filesd', required=True, help='Prometheus file-SD directory')
    parser.add_argument('--alertrule', required=True, help='Alert manager rule directory')
    args = parser.parse_args()
    print(args.__dict__)

    with open(args.template) as file:
        documents = yaml.full_load(file)

        vnf_id = documents.get("vnf_id", "")
        metric_type = documents.get("metric_type", "")
        expresstion = documents.get("expresstion", "")
        threshold_value = documents.get("threshold_value", "")
        operator = documents.get("operator", "")
        action = documents.get("action", "")

        file_sd = FileSD(vnf_id, metric_type)
        file_sd.export_to_file(args.filesd)

        alert_rule = AlertRule(metric_type, expresstion, threshold_value, operator, action)
        alert_rule.export_to_file(args.alertrule)