import pandas as pd
from pathlib import Path
from ej2b2 import read_json_basic, read_json_with_orientation, read_json_and_normalize

current_dir = Path(__file__).parent
BASIC_JSON_PATH = current_dir / "data/ej2b2/ramen-ratings.json"
RECORDS_JSON_PATH = current_dir / "data/ej2b2/ramen-ratings-records.json"
TABLE_JSON_PATH = current_dir / "data/ej2b2/ramen-ratings-table.json"
NORMALIZE_JSON_PATH = current_dir / "data/ej2b2/ramen-ratings-nested.json"


def test_read_json_basic():
    df = read_json_basic(BASIC_JSON_PATH)
    assert isinstance(df, pd.DataFrame), "The returned object is not a pandas DataFrame"
    assert not df.empty, "The DataFrame is empty"


def test_read_json_with_orientation():
    df = read_json_with_orientation(RECORDS_JSON_PATH, orient="records")
    assert isinstance(df, pd.DataFrame), "The returned object is not a pandas DataFrame"
    assert not df.empty, "The DataFrame is empty"


def test_read_json_with_table_orientation():
    df = read_json_with_orientation(TABLE_JSON_PATH, orient="table")
    assert isinstance(df, pd.DataFrame), "The returned object is not a pandas DataFrame"
    assert not df.empty, "The DataFrame is empty"


def test_read_json_and_normalize():
    df = read_json_and_normalize(NORMALIZE_JSON_PATH, record_path=["data"])
    assert isinstance(df, pd.DataFrame), "The returned object is not a pandas DataFrame"
    assert not df.empty, "The DataFrame is empty"
