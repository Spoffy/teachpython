import requests
import json

#Temporary until configurations are implemented
SERVER_IP = "127.0.0.1"

def post(data):
    requests.post(SERVER_IP, data=json.dumps(data))

def post_error(error_info):
    error_info_to_serialise = {
            "trace": error_info.trace,
            "file_path": error_info.file_path,
            "source": error_info.source
    }
    post(error_info_to_serialise)
