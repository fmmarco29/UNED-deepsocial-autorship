import yaml
import json
import time
from pathlib import Path
from typing import List, Dict, Any
from loguru import logger

class HealthCIBCollector:
    """
    Motor de adquisición multifuente para la detección de identidades vinculadas.
    Foco: Twitter/X, Telegram y análisis de infografías.
    """
    
    def __init__(self, config_path: str = "configs/search_config.yaml"):
        self.config = self._load_config(config_path)
        self.output_dir = Path("data/raw")
        self.images_dir = self.output_dir / "infographics"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.images_dir.mkdir(parents=True, exist_ok=True)
        logger.info("Collector Health-CIB inicializado (X + Telegram).")

    def _load_config(self, path: str) -> Dict[str, Any]:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def run_acquisition(self):
        """Ejecuta la recolección coordinada."""
        terms = self.config['search_params']['query_terms']
        logger.info(f"Iniciando captura forense para {len(terms)} núcleos de búsqueda.")
        
        results = []
        for term in terms:
            # Simulación de extracción multifuente
            results.extend(self._collect_from_sources(term))
            time.sleep(0.1)

        self._persist_data(results)

    def _collect_from_sources(self, query: str) -> List[Dict[str, Any]]:
        """Extrae evidencias de múltiples plataformas para un término."""
        return [
            {
                "id": f"ev_{int(time.time())}",
                "query": query,
                "platform": "twitter",
                "author_handle": "user_alpha",
                "text": f"Información sobre {query} detectada en X.",
                "timestamp": "2026-04-23T14:00:00Z",
                "media_metadata": {"type": "infographic", "local_path": "data/raw/infographics/sample.jpg"},
                "behavioral_metadata": {"source": "Twitter for iPhone", "burst_id": "b001"}
            },
            {
                "id": f"ev_{int(time.time())+1}",
                "query": query,
                "platform": "telegram",
                "author_handle": "canal_beta",
                "text": f"Reenvío de {query} en canal de Telegram.",
                "timestamp": "2026-04-23T14:05:00Z",
                "media_metadata": {"type": "infographic", "local_path": "data/raw/infographics/sample.jpg"},
                "behavioral_metadata": {"source": "Telegram Desktop", "burst_id": "b001"}
            }
        ]

    def _persist_data(self, data: List[Dict[str, Any]]):
        output_file = self.output_dir / "health_cib_raw.jsonl"
        with open(output_file, "w", encoding="utf-8") as f:
            for entry in data:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        logger.success(f"Dataset multifuente guardado en {output_file}")

if __name__ == "__main__":
    collector = HealthCIBCollector()
    collector.run_acquisition()
