import os
import pytest
from ej6b1 import count_letters, create_log


@pytest.fixture
def names():
    return ["Juan", "Pedro", "Marta"]


@pytest.fixture
def expected_letter_counts():
    return {
        "J": 1,
        "u": 1,
        "a": 3,
        "n": 1,
        "P": 1,
        "e": 1,
        "d": 1,
        "r": 2,
        "o": 1,
        "M": 1,
        "t": 1,
    }


def test_count_letters(names, expected_letter_counts):
    letter_counts = count_letters(names)
    assert letter_counts == expected_letter_counts, "Incorrect letter counts"


def test_logs_created(names):
    create_log(names)
    assert os.path.exists("production.log"), "Log file not created"


def test_logs_written(names, expected_letter_counts):
    create_log(names)
    with open("production.log", "r") as f:
        lines = f.readlines()
        assert any(f"Letter counts: {expected_letter_counts}" in line for line in lines), "Incorrect letter counts written to log"

