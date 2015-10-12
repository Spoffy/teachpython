from . import config
import json
import requests
import sys
import time
import traceback
import uuid

_message_handlers = dict()
_message_decoders = dict()

def encode(message):
    return json.dumps({
        "user_id": config.USER_ID,
        "time": time.time(),
        "message_type": message.MESSAGE_TYPE,
        "message": message.serialise()
    })

def decode(packet):
    decoder = _message_decoders[packet["message_type"]]
    return decoder(packet["message"])

def on_message_received(packet):
    handle = _message_handlers[packet["message_type"]]
    packet["message"] = decode(packet)
    return handle(packet)

def send(message):
    request = requests.post(config.SERVER_ADDRESS, data=encode(message),
            headers={"content-type": "application/json"})

    try:
      return request.json()
    except ValueError:
      return None

def add_message_handler(type, handler):
    _message_handlers[type] = handler

def add_message_decoder(type, decoder):
    _message_decoders[type] = decoder
