import zmq
import time

def start_bus():
    ctx = zmq.Context()

    frontend = ctx.socket(zmq.SUB)
    frontend.bind("tcp://*:5555")
    frontend.setsockopt_string(zmq.SUBSCRIBE, "")

    backend = ctx.socket(zmq.PUB)
    backend.bind("tcp://*:5556")

    print("[BUS] Message router running...")

    while True:
        packet = frontend.recv()
        backend.send(packet)

if __name__ == "__main__":
    start_bus()