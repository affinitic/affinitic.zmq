#
#   Request-reply service in Python
#   Connects REP socket to tcp://localhost:5560
#   Expects "Hello" from client, replies with "World"
#
import zmq
from subprocess import Popen


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://192.168.99.115:5555")

    while True:
        message = socket.recv()
        print("Received request: %s" % message)
        Popen(message.split('|'))
        socket.send("World")
