import json
from typing import Optional

class PortaPackController:
    def __init__(self, device_path="/dev/ttyACM0"):
        self.device_path = device_path

    def send_custom_signal(self, freq: str, modulation: str, payload: str) -> bool:
        """Envía una señal personalizada via PortaPack Mayhem."""
        cmd = {
            "type": "transmit",
            "freq": freq,
            "mod": modulation,
            "payload": payload
        }
        try:
            with open(self.device_path, "w") as port:
                port.write(json.dumps(cmd))
            return True
        except Exception as e:
            print(f"[PortaPack Error] {str(e)}")
            return False

    def capture_signal(self, freq: str, duration_sec: int = 5) -> Optional[bytes]:
        """Captura señales RAW para análisis posterior."""
        # Implementar usando hackrf_transfer
        pass
from iot_sentinel.core import HackRFFuzzer, PortaPackController

hackrf = HackRFFuzzer()
portapack = PortaPackController()

# Escanear vulnerabilidades
results = hackrf.fuzz_range(RFProtocol.OOK)

# Enviar señal de explotación (si se encuentra vulnerable)
if any(r.is_vulnerable for r in results):
    portapack.send_custom_signal("433M", "OOK", "AABBCCDDEEFF")
