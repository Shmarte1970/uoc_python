import csv
from pathlib import Path
from typing import List, Dict, Union


def load_csv(filepath: Union[str, Path]) -> List[Dict[str, str]]:
    """
    Loads a CSV file and returns a list of dictionaries,
    where each dictionary represents a row.
    """
    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)