import re

def validate_frequency(freq: str) -> str:
    """Verifica que la frecuencia tenga formato válido (ej: '433M')."""
    if not re.match(r"^\d+[MG]Hz?$", freq):
        raise ValueError(f"Formato de frecuencia inválido: {freq}")
    return freq
