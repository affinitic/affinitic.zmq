import zmq
import argparse
import time


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('message')
    parser.add_argument('ip', type=str)
    return parser.parse_args()


def main():
    args = get_args()
    # Prepare our context and sockets
    context = zmq.Context()
    
    socket = context.socket(zmq.REQ)
    socket.connect(args.ip)
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
