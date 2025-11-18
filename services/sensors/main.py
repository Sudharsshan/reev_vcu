import os
from sensor_manager import SensorManager
import zmq
import json
import time

MODE = os.getenv("VCU_MODE", "DEV")

def start():
    sm = SensorManager(mode=MODE)

    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    pub.connect("tcp://localhost:5555")

    seq = 0
    rate = 0.1  # 10 Hz

    while True:
        packet = sm.read_all(seq)
        pub.send_json(packet)

        seq += 1
        time.sleep(rate)

if __name__ == "__main__":
    start()
