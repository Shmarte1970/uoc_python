import pytest
from ej2a1 import simulate_dice_rolls


def test_return_type():
    assert isinstance(
        simulate_dice_rolls(100), dict
    ), "Function should return a dictionary"


def test_keys():
    result = simulate_dice_rolls(100)
    assert all(
        key in result for key in range(1, 7)
    ), "Dictionary should contain keys from 1 to 6"


def test_probabilities_sum_to_one():
    result = simulate_dice_rolls(1000)
    total_prob = sum(result.values())
    assert (
        0.99 <= total_prob <= 1.01
    ), "Total sum of probabilities should be approximately 1"


def test_small_n():
    result = simulate_dice_rolls(1)
    assert (
        len(result) == 6 and sum(result.values()) == 1
    ), "Function should handle n = 1 correctly"


# To run these tests, save this code in a test file (e.g., test_simulate_dice_rolls.py)
# and then execute `pytest` in your terminal.
