import json
import requests
import sys
import time
import uuid

#Temporary until configurations are implemented
SERVER_ADDRESS = "http://127.0.0.1:8080/analytics"
USER_ID = str(uuid.getnode())

_message_handlers = dict()

def encode(message):
    return json.dumps({
        "user_id": USER_ID,
        "time": time.time(),
        "message_type": message.MESSAGE_TYPE,
        "message": message.serialise()
    })

def on_message_received(raw_json):
    try:
        packet = json.loads(raw_json)
        handler = _message_handlers[packet["message_type"]]
        handler(packet["message"])
    except KeyError:
        print("Malformed JSON, unable to handle", file=sys.stderr)

def send(message):
    requests.post(SERVER_ADDRESS, data=encode(message),
            headers={"content-type": "application/json"})

def add_message_handler(type, handler):
    _message_handles[type] = handler
