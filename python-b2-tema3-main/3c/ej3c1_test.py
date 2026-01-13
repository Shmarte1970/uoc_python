from ej3c1 import convert_to_fahrenheit


def test_convert_to_fahrenheit():
    test_cases = [
        (0, 32),
        (10, 50),
        (20, 68),
        (35, 95),
        (45, 113),
        (60, 140),
    ]

    for celsius, expected in test_cases:
        result = convert_to_fahrenheit(celsius)
        assert result == expected, f"Expected {expected} for {celsius}C, got {result}"


def filter_celsius(temperatures):
    return list(filter(lambda x: x < 60, temperatures))


def test_filter_celsius():
    test_temperatures = [54, 84, 38, 104, 101, 107, 55, 1, 38, 31, 109, 6, 91, 46, 16, 28, 74, 102, 20, 39]
    expected_filtered = [54, 38, 55, 1, 38, 31, 6, 46, 16, 28, 20, 39]
    filtered_temperatures = filter_celsius(test_temperatures)
    assert (
        filtered_temperatures == expected_filtered
    ), f"Expected {expected_filtered}, got {filtered_temperatures}"
