# 🛡️ IoT Sentinel - Supercharged IoT Auditing Toolkit
[![License](https://img.shields.io/badge/License-GPLv3_Ethical-blue)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-yellowgreen)](https://python.org)
[![Devices](https://img.shields.io/badge/Devices-Flipper%2C%20HackRF%2C%20ESP32-orange)](https://github.com/KevinDevSecOps/IoT-Sentinel)

**El Swiss Army Knife del hacking ético en IoT**, con soporte para:
- 🐬 Flipper Zero (NFC/Sub-GHz)  
- 📡 HackRF + PortaPack (RF Fuzzing)  
- 📶 ESP32 StickPlus2 (WiFi/BLE)  

> "Por una IoT más segura, sin dejar de ser cool" - KevinDevSecOps

---

## 📦 **Instalación Rápida**
```bash
# Clona el repo
git clone https://github.com/KevinDevSecOps/IoT-Sentinel.git
cd IoT-Sentinel

# Instala dependencias
pip install -r requirements.txt

# Configura dispositivos
python setup.py --flipper /dev/ttyACM0 --esp32 /dev/ttyUSB0
```

---

## 🎯 **Características Estrella**
| Módulo          | Dispositivo       | Función                          |
|-----------------|-------------------|----------------------------------|
| **NFC Auditor** | Flipper Zero      | Clonación ética de tags          |
| **RF Fuzzer**   | HackRF            | Inyección de señales OOK/ASK     |
| **WiFi Spy**    | ESP32 StickPlus2  | Sniffing de paquetes WiFi/BLE    |

---

## 💻 **Ejemplos de Uso**
### 1. Escaneo WiFi con ESP32
```python
from iot_sentinel.core import StickPlus2

esp32 = StickPlus2()
for network in esp32.scan_wifi():
    print(f"📶 {network.ssid} (Canal: {network.channel})")
```
from iot_sentinel.core import StickPlus2

# Configuración
esp32 = StickPlus2(port="/dev/ttyUSB0")

# Captura paquetes durante 30 segundos
packets = esp32.sniff_packets(duration=30)

# Filtra paquetes de interés
deauth_packets = [p for p in packets if p.type == PacketType.WIFI_DEAUTH]
print(f"📡 Capturados {len(deauth_packets)} paquetes de deautenticación")

# Guarda en PCAP (para análisis en Wireshark)
esp32.save_to_pcap(packets, "captura.pcap")

### 2. Fuzzing RF con HackRF
```bash
python -m iot_sentinel.core.hackrf --freq 433M --protocol OOK
```

### 3. Lectura NFC con Flipper
```python
from iot_sentinel.core import FlipperNFC

flipper = FlipperNFC()
tag = flipper.scan_tag()
print(f"🔑 UID: {tag.uid} - Vulnerable: {tag.is_vulnerable}")
```

---

## 📸 **Demo Visual**
![Demo ESP32](docs/images/esp32_demo.gif)  
*Capturando paquetes WiFi en modo promiscuo*

---

## 🛠️ **Configuración de Dispositivos**
| Dispositivo       | Firmware Recomendado | Guía de Instalación              |
|-------------------|----------------------|----------------------------------|
| ESP32 StickPlus2  | [Marauder](https://github.com/justcallmekoko/ESP32Marauder) | `flash_marauder.sh` |
| Flipper Zero      | [Xtreme](https://github.com/Flipper-XFW/Xtreme-Firmware)     | [Wiki](https://flipperzero.one) |

---

## 🤝 **Cómo Contribuir**
1. Haz fork del proyecto.
2. Crea una rama: `git checkout -b feature/nueva-funcion`.
3. Haz commit: `git commit -m "feat: Add X"`.
4. Haz push: `git push origin feature/nueva-funcion`.
5. Abre un **Pull Request**.

---

## 📜 **Licencia y Ética**
Este proyecto usa **GPLv3 + Ethical Clause**:  
```diff
+ Úsalo solo en redes propias o con permiso por escrito.  
- El mal uso conlleva responsabilidad legal (Art. 197 CP, GDPR, etc.).
```

---

## 🌟 **Créditos**
- **KevinDevSecOps** - Autor principal.  
- **Comunidad Marauder** - Firmware ESP32.  
- **Flipper Zero Team** - Inspiración.  

---

```python
# Código con ❤️ para la comunidad
while hacking_ethical == True:
    print("¡Hackea el mundo, mejóralo, y repite!")
```
