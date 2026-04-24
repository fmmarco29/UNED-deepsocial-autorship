from transformers import pipeline
from loguru import logger

class VeracityPredictor:
    """
    Clasificador de veracidad para contenidos de salud en español.
    Evalúa si el contenido textual presenta rasgos de desinformación.
    """
    
    def __init__(self, model_name: str = "Narrativa/roberta-base-bne-fake-news-detection"):
        logger.info(f"Cargando clasificador de veracidad: {model_name}")
        try:
            self.classifier = pipeline("text-classification", model=model_name)
        except Exception as e:
            logger.error(f"Error cargando el modelo: {e}")
            self.classifier = None

    def predict(self, text: str):
        """Predice la veracidad de un texto."""
        if not self.classifier:
            return {"label": "unknown", "score": 0.0}
        return self.classifier(text)[0]

if __name__ == "__main__":
    predictor = VeracityPredictor()
    sample_text = "El grafeno en las vacunas es un secreto de las élites."
    result = predictor.predict(sample_text)
    logger.info(f"Análisis de veracidad: {result}")
