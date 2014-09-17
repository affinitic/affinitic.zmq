import zmq
import socket
from subprocess import Popen


def main():
    
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://192.168.99.115:5555')

    while True:
        message = socket.recv()
        print("Received request: %s" % message)
        command = message.split('|')
        try:
            Popen(command)
            socket.send("Command executed\n")
        except:
            print 'Error while executing the command'
            socket.send("Error while executing the command")
