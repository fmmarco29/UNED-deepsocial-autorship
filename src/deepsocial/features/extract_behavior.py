import pandas as pd
from datetime import datetime
from typing import List, Dict, Any
from loguru import logger

class BehavioralAnalyzer:
    """
    Analizador de rasgos de comportamiento para la detección de coordinación.
    Estudia ráfagas temporales y huellas digitales de dispositivos.
    """
    
    def __init__(self):
        logger.info("Analizador de comportamiento inicializado.")

    def detect_bursts(self, timestamps: List[str], threshold_seconds: int = 60) -> bool:
        """Detecta si existe una ráfaga de actividad coordinada."""
        if not timestamps:
            return False
        
        times = sorted([datetime.fromisoformat(t.replace('Z', '')) for t in timestamps])
        for i in range(1, len(times)):
            diff = (times[i] - times[i-1]).total_seconds()
            if diff < threshold_seconds:
                return True
        return False

    def fingerprint_device_coordination(self, sources: List[str]) -> float:
        """Calcula el ratio de similitud de dispositivos de origen entre cuentas."""
        if not sources:
            return 0.0
        unique_sources = set(sources)
        return 1.0 - (len(unique_sources) / len(sources))

if __name__ == "__main__":
    analyzer = BehavioralAnalyzer()
    sample_times = ["2026-04-23T10:00:00Z", "2026-04-23T10:00:05Z", "2026-04-23T10:00:10Z"]
    is_coordinated = analyzer.detect_bursts(sample_times)
    logger.info(f"Detección de ráfaga temporal: {is_coordinated}")
