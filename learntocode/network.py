import json
import requests
import time
import uuid

#Temporary until configurations are implemented
SERVER_ADDRESS = "http://127.0.0.1:8080/analytics"
USER_ID = str(uuid.getnode())

def encode(message):
    return json.dumps({
        "user_id": USER_ID,
        "time": time.time(),
        "message_type": message.MESSAGE_TYPE,
        "message": message.serialise()
    })

def decode(raw_json):
    pass

def send(message):
    requests.post(SERVER_ADDRESS, data=encode(message),
            headers={"content-type": "application/json"})



