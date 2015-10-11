import requests
import json

#Temporary until configurations are implemented
SERVER_ADDRESS = "http://127.0.0.1"

def post(data):
    requests.post(SERVER_ADDRESS, data=json.dumps(data))

def post_error(debug_info):
    post(debug_info.serialise())
