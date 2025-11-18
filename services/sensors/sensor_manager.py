import time
import json
import importlib
from system.constants import PACKET_SCHEMA_V1 as BASE

class SensorManager:

    def __init__(self, mode="DEV"):
        self.mode = mode

        driver_path = "services.sensors.sim" if mode == "DEV" else "services.sensors.real"

        self.bms = importlib.import_module(f"{driver_path}.fake_bms" if mode=="DEV" else f"{driver_path}.bms_rs232")
        self.ina = importlib.import_module(f"{driver_path}.fake_ina226" if mode=="DEV" else f"{driver_path}.ina226")
        self.mpu = importlib.import_module(f"{driver_path}.fake_mpu" if mode=="DEV" else f"{driver_path}.mpu6050")
        self.temp = importlib.import_module(f"{driver_path}.fake_temp" if mode=="DEV" else f"{driver_path}.ds18b20")
        self.mq2  = importlib.import_module(f"{driver_path}.fake_mq2" if mode=="DEV" else f"{driver_path}.mq2_adc")

    def read_all(self, seq):

        pkt = json.loads(json.dumps(BASE))  # deep copy
        pkt["seq"] = seq
        pkt["timestamp"] = time.time_ns()
        pkt["uptime_sec"] = int(time.monotonic())

        pkt["pack"]["voltage"] = self.bms.read_voltage()
        pkt["pack"]["current_shunt"] = self.ina.read_current()

        pkt["controller"]["rpm"] = 0  # no real rpm yet

        pkt["temp"]["mc_contact"] = self.temp.read_motor()
        pkt["temp"]["battery_ir"] = self.temp.read_ir()

        pkt["environment"]["mq2_left_ppm"] = self.mq2.read_left()
        pkt["environment"]["mq2_right_ppm"] = self.mq2.read_right()

        pkt["mpu"]["accel"] = self.mpu.read_accel()

        return pkt