"""Tests for VisionLanguageSearch."""
from src.core import VisionLanguageSearch
def test_init(): assert VisionLanguageSearch().get_stats()["ops"] == 0
def test_op(): c = VisionLanguageSearch(); c.search(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = VisionLanguageSearch(); [c.search() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = VisionLanguageSearch(); c.search(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = VisionLanguageSearch(); r = c.search(); assert r["service"] == "vision-language-search"
