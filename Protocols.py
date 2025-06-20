from enum import auto, Enum

class ModulationType(Enum):
    DIGITAL = auto()
    ANALOG = auto()

class RFProtocol:
    def __init__(self, name: str, modulation: ModulationType, common_freqs: list):
        self.name = name
        self.modulation = modulation
        self.common_freqs = common_freqs

# Ejemplo de protocolos predefinidos
OOK = RFProtocol("OOK", ModulationType.DIGITAL, ["315M", "433M"])
ASK = RFProtocol("ASK", ModulationType.DIGITAL, ["868M", "915M"])
