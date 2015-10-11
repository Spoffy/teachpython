import json
from . import network

class ErrorDebugInfo():
    MESSAGE_TYPE = "DEBUG_INFO"

    def __init__(self, trace, file_path, source):
        self.trace = trace
        self.file_path = file_path
        self.source = source

    def __str__(self):
        return "\n".join([str(self.file_path), str(self.source), str(self.trace)])

    def serialise(self):
        return {
            "trace": self.trace,
            "file_path": self.file_path,
            "source": self.source
        }

def deserialise_debug_info(data):
    return ErrorDebugInfo(data["trace"], data["file_path"], data["source"])

def exception_handler(debug_info, exception_class):
    network.send(debug_info)

def message_received_handler(data):
    debug_info = deserialise_debug_info(data)
    print(debug_info)

network.add_message_handler(ErrorDebugInfo.MESSAGE_TYPE, message_received_handler)
