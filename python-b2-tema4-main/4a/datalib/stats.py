from typing import List, Dict


def mean(data: List[Dict], key: str) -> float:
    """
    Calculates the mean of numeric values for a given key.
    """
    values = [float(item[key]) for item in data]
    return sum(values) / len(values)


def median(data: List[Dict], key: str) -> float:
    """
    Calculates the median of numeric values for a given key.
    """
    values = sorted(float(item[key]) for item in data)
    n = len(values)
    mid = n // 2

    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    return values[mid]