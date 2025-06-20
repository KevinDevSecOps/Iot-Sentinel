# 🛡️ IoT Sentinel - Ethical IoT Auditing Toolkit
[![License: GPLv3+Ethical](https://img.shields.io/badge/License-GPLv3_Ethical-blue.svg)](https://github.com/KevinDevSecOps/IoT-Sentinel/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-yellowgreen)](https://www.python.org/)
[![Platforms](https://img.shields.io/badge/Platforms-Flipper%20Zero%2C%20HackRF%2C%20ESP32-orange)](https://github.com/KevinDevSecOps/IoT-Sentinel)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)](CONTRIBUTING.md)

**Un sistema integrado de auditoría ética para redes IoT usando Flipper Zero, HackRF y ESP32.**  
*"Hackea el mundo físico... con responsabilidad"* 🔐

---

## 📌 Tabla de Contenidos
- [Características](#-características)
- [Dispositivos Soportados](#-dispositivos-soportados)
- [Instalación](#-instalación)
- [Uso Rápido](#-uso-rápido)
- [Demo](#-demo)
- [Roadmap](#-roadmap)
- [Licencia](#-licencia)
- [Contribuir](#-contribuir)

---

## ✨ Características
| Módulo | Tecnología | Función |
|--------|-----------|---------|
| **RFID/NFC Auditor** | Flipper Zero | Detección de tags clonables y credenciales inseguras |
| **RF Fuzzer** | HackRF + PortaPack | Pruebas de señales en 315/433/868MHz |
| **WiFi/BLE Sniffer** | ESP32 (StickPlus2) | Análisis de dispositivos IoT inseguros |
| **Reporte Automatizado** | Python + LaTeX | Generación de informes PDF profesionales |

---

## 📟 Dispositivos Soportados
| Dispositivo | Firmware Recomendado | Uso Principal |
|-------------|----------------------|---------------|
| Flipper Zero | [Xtreme Firmware](https://github.com/Flipper-XFW/Xtreme-Firmware) | RFID/NFC/Sub-GHz |
| HackRF One | [Mayhem PortaPack](https://github.com/eried/portapack-mayhem) | RF Fuzzing |
| ESP32 StickPlus2 | [ESP32 Marauder](https://github.com/justcallmekoko/ESP32Marauder) | WiFi/BLE Audit |

---

## ⚙️ Instalación
```bash
# Clonar el repositorio
git clone https://github.com/KevinDevSecOps/IoT-Sentinel.git
cd IoT-Sentinel

# Instalar dependencias
pip install -r requirements.txt

# Configurar dispositivos
python setup.py --flipper /dev/ttyACM0 --hackrf serial:12345
```

---

## 🚀 Uso Rápido
### Escaneo NFC básico (Flipper Zero)
```python
from iot_sentinel import FlipperAudit

flipper = FlipperAudit()
flipper.scan_nfc(output_format="json")
```

### Fuzzing RF (HackRF)
```bash
python3 -m iot_sentinel.rf_fuzzer --freq 433.92M --protocol OOK --timeout 60
```
### 🎯 Características
- Soporta protocolos **OOK, ASK, FSK**.
- Escaneo por rangos de frecuencia con **multihilo**.
- Modo ético: Incluye `stop()` para abortar operaciones.

### 🛠️ Uso Básico
```python
from iot_sentinel.core import HackRFFuzzer, RFProtocol

fuzzer = HackRFFuzzer(min_freq="300M", max_freq="900M")
result = fuzzer.fuzz_single("433M", RFProtocol.OOK)
print(f"Vulnerable: {result.is_vulnerable}")
---

## 📸 Demo
![Demo GIF](docs/images/demo.gif)  
*Ejemplo: Detección de tag NFC vulnerable*

---

## 🗺️ Roadmap
- [x] Soporte para Flipper Zero (NFC/Sub-GHz)
- [ ] Integración con Wireshark (ESP32)
- [ ] Módulo de análisis de señales digitales (HackRF)
- [ ] Dockerización del entorno

---

## 📜 Licencia
Este proyecto usa **GNU GPLv3 + Ethical Clause** ([Ver LICENSE](LICENSE)).  
⚠️ **Importante**: 
```diff
- SOLO para pruebas autorizadas. El uso no ético anula la licencia.
```

---

## 🤝 Contribuir
1. Haz fork del proyecto
2. Crea una rama: `git checkout -b feature/nueva-funcion`
3. Haz commit: `git commit -m "feat: Añade X"`
4. Haz push: `git push origin feature/nueva-funcion`
5. Abre un **Pull Request**

---

## 🌟 Créditos
- **KevinDevSecOps** - Autor principal
- **Comunidad Flipper Zero** - Firmware e inspiración

---

```python
# Código con ❤️ para hackers éticos
while world.needs_securing():
    iot_sentinel.audit(world)
```
