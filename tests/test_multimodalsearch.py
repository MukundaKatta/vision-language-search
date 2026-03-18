"""Tests for MultimodalSearch."""
import pytest
from src.multimodalsearch import MultimodalSearch

def test_init():
    obj = MultimodalSearch()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = MultimodalSearch()
    result = obj.index_document(input="test")
    assert result["processed"] is True
    assert result["operation"] == "index_document"

def test_multiple_ops():
    obj = MultimodalSearch()
    for m in ['index_document', 'index_image', 'search_text']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = MultimodalSearch()
    r1 = obj.index_document(key="same")
    r2 = obj.index_document(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = MultimodalSearch()
    obj.index_document()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = MultimodalSearch()
    obj.index_document(x=1)
    obj.index_image(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats
