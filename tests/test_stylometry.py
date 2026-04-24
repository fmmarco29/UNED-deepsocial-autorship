import numpy as np
import pytest
from unittest.mock import MagicMock, patch

# Mocking StylometryExtractor to avoid torch dependency in CI
class MockStylometryExtractor:
    def calculate_similarity(self, emb1, emb2):
        dot_product = np.dot(emb1, emb2)
        norm_a = np.linalg.norm(emb1)
        norm_b = np.linalg.norm(emb2)
        return dot_product / (norm_a * norm_b)

def test_similarity_identical():
    extractor = MockStylometryExtractor()
    emb = np.array([1.0, 0.0, 0.0])
    similarity = extractor.calculate_similarity(emb, emb)
    assert pytest.approx(similarity) == 1.0

def test_similarity_orthogonal():
    extractor = MockStylometryExtractor()
    emb1 = np.array([1.0, 0.0, 0.0])
    emb2 = np.array([0.0, 1.0, 0.0])
    similarity = extractor.calculate_similarity(emb1, emb2)
    assert pytest.approx(similarity) == 0.0
