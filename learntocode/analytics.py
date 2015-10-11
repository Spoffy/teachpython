import json
from . import network

class ErrorDebugInfo(network.Message):
    def __init__(self, trace, file_path, source):
        self.trace = trace
        self.file_path = file_path
        self.source = source

    def __str__(self):
        return "\n".join([str(self.file_path), str(self.source), str(self.trace)])

    def to_json(self):
        return json.dumps({
            "trace": self.trace,
            "file_path": self.file_path,
            "source": self.source
        })

def debug_info_handler(debug_info, exception_class):
    network.send_message(debug_info)
