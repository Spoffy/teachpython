import json
import requests
import time
import uuid

#Temporary until configurations are implemented
SERVER_ADDRESS = "http://127.0.0.1:8080/analytics"
USER_ID = str(uuid.getnode())

class Message:
    def to_dict():
        """This should be overridden by inheriting classes"""
        return dict()

def send(data):
    packet = {
            "user_id": USER_ID,
            "time": time.time(),
            "message": data
    }
    requests.post(SERVER_ADDRESS, data=json.dumps(packet), 
            headers={"content-type": "application/json"})

def send_message(message):
    send(message.to_dict())
