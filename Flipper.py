import serial
from dataclasses import dataclass
from enum import Enum

class NFCTagType(Enum):
    MIFARE_CLASSIC = "Mifare Classic"
    NTAG_21x = "NTAG213/215/216"

@dataclass
class NFCTag:
    uid: str
    tag_type: NFCTagType
    is_vulnerable: bool

class FlipperNFC:
    def __init__(self, port: str = "/dev/ttyACM0", baudrate: int = 115200):
        self.serial = serial.Serial(port, baudrate, timeout=1)

    def scan_tag(self) -> NFCTag:
        """Detecta y analiza tags NFC."""
        self.serial.write(b"nfc scan\n")
        response = self.serial.read_until(b"Done").decode()

        if "UID:" not in response:
            raise ValueError("No NFC tag detected")

        uid = response.split("UID:")[1].split("\n")[0].strip()
        return NFCTag(
            uid=uid,
            tag_type=self._detect_tag_type(response),
            is_vulnerable=self._check_weak_uid(uid)
        )

    def _detect_tag_type(self, response: str) -> NFCTagType:
        return NFCTagType.MIFARE_CLASSIC if "Mifare Classic" in response else NFCTagType.NTAG_21x

    def _check_weak_uid(self, uid: str) -> bool:
        weak_uids = ["00000000", "FFFFFFFF", "12345678"]
        return uid.upper() in weak_uids
