import json
import io
import os

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

class FileSD:
    def __init__(self, ip_address, metric_type):
        self._ip_address = ip_address
        self._metric_type = metric_type

    def _parse_to_object(self):
        data = {
            "labels": {
                "job": self._metric_type
            },
            "targets": [self._ip_address]
        }
        return data

    def export_to_file(self, file):
        if os.path.exists(file):
            with open(file) as data_file:
                try:
                    data = json.load(data_file)
                except ValueError:
                    data = []
            
        else: 
            data = [] 
        data.append(self._parse_to_object())
        
        with io.open(file, "w+", encoding='utf8') as outfile:
            str_ = json.dumps(data,
                            indent=4, sort_keys=True,
                            separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))

            