import re

class FrequencyValidator:
    @staticmethod
    def validate(freq: str) -> bool:
        """Valida formato de frecuencia (ej: '433M')."""
        return bool(re.match(r"^\d+[MG]Hz?$", freq))

class EthicalGuard:
    BANNED_FREQS = ["108M", "137M", "433M"]  # Frecuencias prohibidas

    @classmethod
    def check_frequency(cls, freq: str) -> None:
        """Lanza excepción si la frecuencia es prohibida."""
        if freq in cls.BANNED_FREQS:
            raise ValueError(f"¡Frecuencia {freq} prohibida por ley!")
