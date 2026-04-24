import torch
from transformers import AutoTokenizer, AutoModel
import numpy as np
from typing import List
from loguru import logger

class StylometryExtractor:
    """
    Extrae rasgos estilométricos utilizando modelos de lenguaje.
    Utiliza RoBERTa-base-bne para la representación densa del estilo de escritura.
    """
    
    def __init__(self, model_name: str = "PlanTL-GOB-ES/roberta-base-bne"):
        logger.info(f"Cargando modelo de estilometría: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.model.eval()

    def get_stylometric_embedding(self, text: str) -> np.ndarray:
        """
        Convierte un texto en un vector denso (embedding) que captura 
        aspectos semánticos y sintácticos del autor.
        """
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Usamos el 'mean pooling' de la última capa oculta como representación
        embeddings = outputs.last_hidden_state.mean(dim=1).numpy()
        return embeddings.flatten()

    def calculate_similarity(self, emb1: np.ndarray, emb2: np.ndarray) -> float:
        """Calcula la similitud de coseno entre dos huellas dactilares estilométricas."""
        dot_product = np.dot(emb1, emb2)
        norm_a = np.linalg.norm(emb1)
        norm_b = np.linalg.norm(emb2)
        return dot_product / (norm_a * norm_b)

if __name__ == "__main__":
    extractor = StylometryExtractor()
    t1 = "El bicarbonato es la cura definitiva para el cáncer que no quieren que sepas."
    t2 = "La medicina oficial oculta que el bicarbonato cura el cáncer de forma natural."
    
    e1 = extractor.get_stylometric_embedding(t1)
    e2 = extractor.get_stylometric_embedding(t2)
    
    sim = extractor.calculate_similarity(e1, e2)
    logger.info(f"Similitud estilística entre cuentas: {sim:.4f}")
