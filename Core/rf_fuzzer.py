from enum import Enum
import subprocess

class RFProtocol(Enum):
    OOK = "ook"
    ASK = "ask"

class HackRFFuzzer:
    def __init__(self, freq="433.92M", power=10):
        self.freq = freq
        self.power = power

    def send_pulse(self, protocol: RFProtocol, duration_ms=100):
        """Envía una señal RF usando hackrf_transfer."""
        cmd = [
            "hackrf_transfer",
            "-f", self.freq,
            "-x", str(self.power),
            "-t", f"/dev/zero",
            "-p", protocol.value,
            "-l", "64",
            "-a", "1"
        ]
        subprocess.run(cmd, timeout=duration_ms/1000)
