import pytest
from typing import List
from ej6b3 import check_primes


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4, 5], [False, True, True, False, True]),
        ([0, 1, 2, 3, 4, 5], [False, False, True, True, False, True]),
        ([1], [False]),
    ],
)
def test_check_primes(nums: List[int], expected: List[bool]):
    assert check_primes(nums) == expected, "The check_primes function does not return the expected list"
