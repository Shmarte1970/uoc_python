import pytest
from ej6b2 import average_of_even_numbers


def test_average_of_even_numbers_with_positive_numbers():
    numbers = [2, 3, 4, 5, 6]
    assert average_of_even_numbers(numbers) == 4.0, "Average of even numbers should be 4.0 for input [2, 3, 4, 5, 6]"


def test_average_of_even_numbers_with_negative_numbers():
    numbers = [-2, -3, -4, -5, -6]
    assert average_of_even_numbers(numbers) == -4.0, "Average of even numbers should be -4.0 for input [-2, -3, -4, -5, -6]"


def test_average_of_even_numbers_with_no_even_numbers():
    numbers = [1, 3, 5, 7]
    assert average_of_even_numbers(numbers) == 0.0, "Average of even numbers should be 0.0 for input [1, 3, 5, 7]"


def test_average_of_even_numbers_with_empty_list():
    numbers = []
    assert average_of_even_numbers(numbers) == 0.0, "Average of even numbers should be 0.0 for input []"


def test_average_of_even_numbers_with_float_numbers():
    numbers = [2.0, 3.0, 4.0, 5.0, 6.0]
    assert average_of_even_numbers(numbers) == 4.0, "Average of even numbers should be 4.0 for input [2.0, 3.0, 4.0, 5.0, 6.0]"


