from bottle import post, run, request
from learntocode import network

@post("/analytics")
def print_analytics():
    return network.on_message_received(request.json)

run(host="0.0.0.0", port=8080)
