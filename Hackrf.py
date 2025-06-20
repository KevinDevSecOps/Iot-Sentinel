import subprocess
from enum import Enum
from dataclasses import dataclass
from typing import List

class RFProtocol(Enum):
    OOK = "ook"
    ASK = "ask"
    FSK = "fsk"

@dataclass
class FuzzingResult:
    frequency: str
    protocol: RFProtocol
    is_vulnerable: bool

class HackRFAuditor:
    def __init__(self, min_freq: str = "300M", max_freq: str = "900M", max_power: int = 20):
        self.min_freq = min_freq
        self.max_freq = max_freq
        self.max_power = max_power

    def fuzz_single(self, freq: str, protocol: RFProtocol) -> FuzzingResult:
        """Envía una señal en una frecuencia específica."""
        cmd = [
            "hackrf_transfer",
            "-f", freq,
            "-x", str(self.max_power),
            "-t", "/dev/null",
            "-p", protocol.value,
            "-l", "64",
            "-a", "1"
        ]
        try:
            subprocess.run(cmd, check=True, timeout=5)
            return FuzzingResult(freq, protocol, True)
        except subprocess.CalledProcessError:
            return FuzzingResult(freq, protocol, False)

    def fuzz_range(self, protocol: RFProtocol, step: str = "1M") -> List[FuzzingResult]:
        """Escanea un rango de frecuencias."""
        # Implementación con ThreadPoolExecutor (como en el ejemplo anterior)
        pass
