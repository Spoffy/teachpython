from .. import config, network

class Move:
    MESSAGE_TYPE = "MOVE_ORDER"

    def __init__(self, name, dir, amount):
      self.name = name
      self.dir = dir
      self.amount = amount

    def serialise(self):
      return {
        "name": self.name,
        "dir": self.dir,
        "amount": self.amount
      }

def deserialise_move(data):
    return Move(data["name"], data["dir"], data["amount"])

def move(name, dir, amount):
    move = Move(name, dir, amount)
    network.send(move)

def message_received_handler(packet):
    move = packet["message"]
    print("MOVE: ", str(move.name), str(move.dir), str(move.amount))

network.add_message_decoder(Move.MESSAGE_TYPE, deserialise_move)
network.add_message_handler(Move.MESSAGE_TYPE, message_received_handler)
