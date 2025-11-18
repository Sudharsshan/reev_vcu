PACKET_SCHEMA_V1 = {
    "seq": 0,
    "timestamp": 0,
    "uptime_sec": 0,

    "pack": {
        "voltage": 0.0,
        "current_shunt": 0.0
    },

    "controller": {
        "rpm": 0
    },

    "temp": {
        "mc_contact": 0.0,
        "battery_ir": 0.0
    },

    "environment": {
        "mq2_left_ppm": 0,
        "mq2_right_ppm": 0
    },

    "mpu": {
        "accel": {"x": 0.0, "y": 0.0, "z": 0.0}
    },

    "faults": {
        "active": 0,
        "severity": 0,
        "list": []
    },

    "vcu": {
        "version": "0.1",
        "mode": "DEV",
        "sample_rate": 10
    }
}
