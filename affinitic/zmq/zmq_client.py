import zmq
import argparse
import time

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('message')
    return parser.parse_args()


def main():
    args = get_args()

    # Prepare our context and sockets
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://192.168.99.115:5555")
    
    received = False
    socket.send(args.message)

    for j in range(36000):
        time.sleep(0.1)

        try:
            msg = socket.recv(zmq.NOBLOCK)
            print msg + 'msg sended'
            break
        except zmq.ZMQError, e:
            if e.errno == zmq.EAGAIN:
                # No response received
                pass
            else:
                raise e