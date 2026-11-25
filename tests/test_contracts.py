"""Checks each module must pass once it is implemented.

Each test is skipped until its owner removes the skip and writes the check.
"""
import pytest


@pytest.mark.skip(reason="Member 1: enable once features.py is implemented")
def test_features_do_not_use_the_future():
    """Removing later months must not change the features of earlier months."""


@pytest.mark.skip(reason="Member 1: enable once features.py is implemented")
def test_target_is_next_month_return():
    """TARGET at month t equals price(t+1) / price(t) - 1."""


@pytest.mark.skip(reason="Member 2: enable once split.py is implemented")
def test_split_is_chronological():
    """Every training month comes before every test month."""


@pytest.mark.skip(reason="Member 2: enable once evaluate.py is implemented")
def test_baseline_predicts_training_mean():
    """The baseline predicts the training-set average for every test row."""
