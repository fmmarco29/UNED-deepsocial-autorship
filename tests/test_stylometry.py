import numpy as np
import torch
import pytest
from src.deepsocial.features.extract_stylometry import StylometryExtractor
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_extractor():
    with patch('transformers.AutoTokenizer.from_pretrained'), \
         patch('transformers.AutoModel.from_pretrained'):
        extractor = StylometryExtractor()
        # Mocking the model response
        mock_output = MagicMock()
        mock_output.last_hidden_state.mean.return_value = torch.tensor([[0.1, 0.2, 0.3]])
        extractor.model.return_value = mock_output
        extractor.tokenizer.return_value = {"input_ids": torch.tensor([[1, 2, 3]])}
        return extractor

def test_similarity_identical():
    extractor = StylometryExtractor.__new__(StylometryExtractor)
    emb = np.array([1.0, 0.0, 0.0])
    similarity = extractor.calculate_similarity(emb, emb)
    assert pytest.approx(similarity) == 1.0

def test_similarity_orthogonal():
    extractor = StylometryExtractor.__new__(StylometryExtractor)
    emb1 = np.array([1.0, 0.0, 0.0])
    emb2 = np.array([0.0, 1.0, 0.0])
    similarity = extractor.calculate_similarity(emb1, emb2)
    assert pytest.approx(similarity) == 0.0
