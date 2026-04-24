import open_clip
import torch
from PIL import Image
from pathlib import Path
from loguru import logger

class VisualFeatureExtractor:
    """
    Extractor de características visuales para análisis multimodal.
    Utiliza CLIP para generar embeddings alineados con el dominio textual.
    """
    
    def __init__(self, model_name: str = "ViT-B-32", pretrained: str = "laion2b_s34b_b79k"):
        logger.info(f"Cargando modelo CLIP: {model_name}")
        self.model, _, self.preprocess = open_clip.create_model_and_transforms(model_name, pretrained=pretrained)
        self.tokenizer = open_clip.get_tokenizer(model_name)

    def extract_visual_embedding(self, image_path: str):
        """Convierte una imagen en un vector de características."""
        if not Path(image_path).exists():
            logger.warning(f"Imagen no encontrada: {image_path}")
            return None
            
        image = self.preprocess(Image.open(image_path)).unsqueeze(0)
        with torch.no_grad():
            image_features = self.model.encode_image(image)
        
        return image_features.numpy().flatten()

if __name__ == "__main__":
    # Este script requiere tener imágenes en data/raw/images/
    extractor = VisualFeatureExtractor()
    logger.info("Módulo visual cargado correctamente.")
