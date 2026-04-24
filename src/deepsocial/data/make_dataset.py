import json
import time
from pathlib import Path
from loguru import logger

class MultimodalMultisourceIngestor:
    """
    Motor de creación de datasets para investigación forense.
    Especializado en la alineación de señales de X (Twitter) y Telegram.
    """
    
    def __init__(self, base_path: str = "data/raw"):
        self.base_path = Path(base_path)
        self.infographics_path = self.base_path / "infographics"
        self.base_path.mkdir(parents=True, exist_ok=True)
        self.infographics_path.mkdir(parents=True, exist_ok=True)
        logger.info("Ingestor Multimodal/Multifuente listo.")

    def ingest_coordinated_event(self, x_data: dict, tg_data: dict, image_path: str):
        """
        Fusiona datos de dos fuentes y una señal visual en un único registro.
        Esto demuestra la capacidad de crear datasets complejos.
        """
        event = {
          "timestamp_capture": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
          "sources": ["twitter", "telegram"],
          "content": {
              "twitter": x_data,
              "telegram": tg_data
          },
          "visual_signal": {
              "local_path": image_path,
              "type": "infographic"
          },
          "is_labeled": False # Preparado para etiquetado humano o automático
        }
        
        self._save_event(event)
        logger.success(f"Evento coordinado capturado y alineado: {event['sources']}")

    def _save_event(self, event: dict):
        output_file = self.base_path / "health_cib_multimodal.jsonl"
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    ingestor = MultimodalMultisourceIngestor()
    # Demostración de alineación multifuente
    x_sample = {"user": "salud_alternativa", "text": "Cura natural detectada.", "time": "10:00"}
    tg_sample = {"channel": "InfoLibre", "text": "Reenviado: Cura natural.", "time": "10:05"}
    ingestor.ingest_coordinated_event(x_sample, tg_sample, "data/raw/infographics/sample_01.jpg")
