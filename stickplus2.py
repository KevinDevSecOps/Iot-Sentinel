#!/usr/bin/env python3
import serial
import json
from dataclasses import dataclass
from enum import Enum, auto

class WiFiEncryption(Enum):
    OPEN = auto()
    WEP = auto()
    WPA2 = auto()
    WPA3 = auto()

@dataclass
class WiFiNetwork:
    ssid: str
    bssid: str
    channel: int
    encryption: WiFiEncryption
    clients: int = 0

class StickPlus2:
    def __init__(self, port: str = "/dev/ttyUSB0", baudrate: int = 115200):
        self.serial = serial.Serial(port, baudrate, timeout=5)
        self._send_command("mode wifi")

    def _send_command(self, cmd: str) -> str:
        """Envía comandos al firmware Marauder"""
        self.serial.write(f"{cmd}\n".encode())
        return self.serial.read_until(b"END").decode()

    def scan_wifi(self) -> list[WiFiNetwork]:
        """Escanea redes WiFi y devuelve objetos estructurados"""
        output = self._send_command("scan")
        networks = []
        
        for line in output.splitlines():
            if "SSID:" in line:
                parts = line.split()
                networks.append(
                    WiFiNetwork(
                        ssid=parts[1],
                        bssid=parts[3],
                        channel=int(parts[5]),
                        encryption=WiFiEncryption[parts[7]]
                    )
                )
        return networks

    def deauth(self, bssid: str, count: int = 1) -> bool:
        """Envía paquetes de deautenticación (solo redes propias/CTFs)"""
        if not bssid.startswith("00:"):  # Demo, no redes reales
            raise ValueError("¡Solo para redes autorizadas!")
        return "OK" in self._send_command(f"deauth {bssid} {count}")

    def sniff_ble(self, timeout: int = 30) -> dict:
        """Captura anuncios BLE y los devuelve como JSON"""
        output = self._send_command(f"ble_scan {timeout}")
        return json.loads(output)
