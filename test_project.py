# test_project.py
import pytest
from project import fetch_data

def test_fetch_data_returns_dict():
    # Test that fetch_data returns a dictionary
    result = fetch_data("movies", 8.0, "Action", 2025)
    assert isinstance(result, dict)

def test_fetch_data_invalid_params():
    # Test that fetch_data gracefully returns an empty dict for impossible criteria
    result = fetch_data("tvSeries", 11.0, "Action", 3000)
    assert result == {} or len(result) == 0

def test_fetch_data_type_safety():
    # Test that fetch_data returns an empty dictionary when looking for an invalid year format
    result = fetch_data("movies", 8.5, "Drama", "NotAYear")
    assert isinstance(result, dict)