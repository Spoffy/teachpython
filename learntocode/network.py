import requests
import json

#Temporary until configurations are implemented
SERVER_ADDRESS = "http://127.0.0.1"

class Message:
    _default_message = dict()

    def to_json():
        return json.dumps(_default_message)

def send(data):
    requests.post(SERVER_ADDRESS, data=json.dumps(data))

def send_message(debug_info):
    send(debug_info.to_json())
