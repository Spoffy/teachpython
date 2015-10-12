import json
from .. import network

_moves = {}
_routines = {}

class DancePacket:
  MESSAGE_TYPE = "DANCE_PACKET"

  def __init__(self, data):
    self.data = data

  def serialise(self):
    return self.data

def deserialise_dance_packet(data):
  return data

network.add_message_decoder(DancePacket.MESSAGE_TYPE, deserialise_dance_packet)

def list_available_moves():
  return network.send(DancePacket({"type": "list_moves"}))

def list_routines():
  return network.send(DancePacket({"type": "list_routines"}))

def add_dance_move(name, description):
  return network.send(DancePacket({
    "type": "add_move",
    "name": name,
    "desc": description
  }))

def add_dance_routine(name, moves=[]):
  return network.send(DancePacket({
    "type": "add_routine",
    "name": name,
    "moves": moves
  }))

def get_dance_routine(name):
  return network.send(DancePacket({
    "type": "get_routine",
    "name": name
  }))

def add_move_to_routine(routine, move):
  return network.send(DancePacket({
    "type": "add_move_to_routine",
    "routine": routine,
    "move": move
  }))

_handlers = {}

def server_list_moves(dance_packet):
  return json.dumps(_moves)
_handlers["list_moves"] = server_list_moves

def server_list_routines(dance_packet):
  return json.dumps(_routines)
_handlers["list_routines"] = server_list_moves

def server_add_move(dance_packet):
  _moves[dance_packet["name"]] = dance_packet["desc"]
_handlers["add_move"] = server_add_move

def server_add_routine(dance_packet):
  _routines[dance_packet["name"]] = dance_packet["moves"]
_handlers["add_routine"] = server_add_routine

def server_get_routine(dance_packet):
  return json.dumps(_routines[dance_packet["name"]])
_handlers["get_routine"] = server_get_routine

def server_add_move_to_routine(dance_packet):
  _routines[dance_packet["routine"]].append(dance_packet["move"])
_handlers["add_move_to_routine"] = server_add_move_to_routine


def message_received_handler(packet):
  dance_packet = packet["message"]
  packet_type = dance_packet["type"]
  return _handlers[packet_type](dance_packet)
  
network.add_message_handler(DancePacket.MESSAGE_TYPE, message_received_handler)
