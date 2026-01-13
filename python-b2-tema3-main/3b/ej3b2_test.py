import pytest
from ej3b2 import LogMethodCalls


def simple_function(x, y):
    return x + y


def test_LogMethodCalls_decorates_function():
    decorator = LogMethodCalls(print_logs=True)
    decorated_function = decorator(
        simple_function
    )  # Usa la función de utilidad renombrada
    assert (
        decorated_function(2, 3) == 5
    ), "The decorated function should return the result of 2 + 3 even with print_logs=True"


def test_LogMethodCalls_with_print_logs_false():
    decorator = LogMethodCalls(print_logs=False)
    decorated_function = decorator(
        simple_function
    )  # Usa la función de utilidad renombrada
    assert (
        decorated_function(2, 3) == 5
    ), "The decorated function should return the result of 2 + 3 even with print_logs=False"
