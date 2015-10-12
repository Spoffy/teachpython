from . import config, network
import json
import os
import os.path as path
import time
import traceback

class ErrorDebugInfo():
    MESSAGE_TYPE = "DEBUG_INFO"

    def __init__(self, trace, file_path, source):
        self.trace = trace
        self.file_path = file_path
        self.source = source

    def __str__(self):
        return "\n".join([str(self.file_path), str(self.source), str(self.trace)])

    #Required to be sent using network.send
    def serialise(self):
        """Converts this class to a dictionary representation"""
        return {
            "trace": self.trace,
            "file_path": self.file_path,
            "source": self.source
        }

def deserialise_debug_info(data):
    return ErrorDebugInfo(data["trace"], data["file_path"], data["source"])

def exception_handler(debug_info, exception_class):
    network.send(debug_info)

def message_received_handler(packet):
    sanitised_name = path.basename(packet["user_id"]).replace("/", "")
    log_path = path.join(config.USER_ERROR_LOG_PATH, sanitised_name)
    debug_info = packet["message"]

    print("ANALYTICS: Error received from: ", sanitised_name)
    try:
      os.makedirs(config.USER_ERROR_LOG_PATH, exist_ok=True)
      with open(log_path, "a") as dest_file:
        print("------", file=dest_file)
        print(time.asctime(time.gmtime(packet["time"])), file=dest_file)
        print("File: ", debug_info.file_path, file=dest_file)
        print("------", file=dest_file)
        print("Trace: ", debug_info.trace, file=dest_file)
        print("------", file=dest_file)
        print("Source: ", debug_info.source, file=dest_file)
        print("------", file=dest_file)
        print("\n\n\n", file=dest_file)
    except IOError:
      traceback.print_exc()

network.add_message_decoder(ErrorDebugInfo.MESSAGE_TYPE, deserialise_debug_info)
network.add_message_handler(ErrorDebugInfo.MESSAGE_TYPE, message_received_handler)

