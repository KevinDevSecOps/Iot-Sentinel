import serial
from dataclasses import dataclass

@dataclass
class NFCTag:
    uid: str
    is_vulnerable: bool

class FlipperAudit:
    def __init__(self, port="/dev/ttyACM0"):
        self.port = serial.Serial(port, baudrate=115200, timeout=1)

    def scan_nfc(self) -> NFCTag:
        """Detecta tags NFC y verifica vulnerabilidades."""
        self.port.write(b"nfc scan\n")
        response = self.port.read_until(b"Done").decode()
        
        if "UID:" in response:
            uid = response.split("UID:")[1].split("\n")[0].strip()
            return NFCTag(uid, self._check_vulnerability(uid))
        raise Exception("Tag no detectado")

    def _check_vulnerability(self, uid: str) -> bool:
        """Verifica si el UID es común (ej: 00000000)."""
        return uid in ["00000000", "FFFFFFFF"]
