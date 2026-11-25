"""Tests for src/data.py (implemented). Run all tests with: python -m pytest -q"""
from src.data import load_clean

EXPECTED = ["price", "dividend", "earnings", "cpi", "long_rate", "pe10"]


def test_columns_and_order():
    df = load_clean()
    assert list(df.columns) == EXPECTED
    assert df.index.is_monotonic_increasing
    assert not df.index.duplicated().any()


def test_no_zero_placeholders():
    df = load_clean()
    assert (df[EXPECTED] > 0).all().all()
