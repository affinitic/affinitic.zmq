import zmq
from subprocess import Popen
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip', type=str)
    return parser.parse_args()


def main():
    args = get_args()
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(args.ip)

    while True:
        message = socket.recv()
        print("Received request: %s" % message)
        command = message.split('|')
        try:
            Popen(command)
            socket.send("Command executed\n")
        except:
            print 'Error while executing the command\n'
            socket.send("Error while executing the command")
