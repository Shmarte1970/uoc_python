import pandas as pd
from pathlib import Path
from ej2b1 import (
    read_csv_basic,
    read_csv_header_issue,
    read_csv_multi_index,
    read_csv_custom_separator,
)

# Rutas de los archivos CSV para las pruebas
current_dir = Path(__file__).parent
BASIC_CSV_PATH = current_dir / "data/ej2b1/ramen-ratings.csv"
HEADER_ISSUE_CSV_PATH = current_dir / "data/ej2b1/ramen_ratings_with_header_issue.csv"
MULTI_INDEX_CSV_PATH = current_dir / "data/ej2b1/ramen_ratings_multi_index.csv"
SEMICOLON_CSV_PATH = current_dir / "data/ej2b1/ramen_ratings_decimal_comma.csv"


def test_read_csv_basic():
    df = read_csv_basic(BASIC_CSV_PATH)
    assert isinstance(df, pd.DataFrame), "The returned object is not a pandas DataFrame"
    assert not df.empty, "The DataFrame is empty"


def test_read_csv_header_issue():
    df = read_csv_header_issue(HEADER_ISSUE_CSV_PATH, header_row=3)
    assert isinstance(df, pd.DataFrame), "The returned object is not a pandas DataFrame"
    assert not df.empty, "The DataFrame is empty"
    assert "Brand" in df.columns, "The 'Brand' column is not present in the DataFrame"


def test_read_csv_multi_index():
    df = read_csv_multi_index(MULTI_INDEX_CSV_PATH, index_cols=["Brand", "Style"])
    assert isinstance(df, pd.DataFrame), "The returned object is not a pandas DataFrame"
    assert not df.empty, "The DataFrame is empty"
    assert isinstance(
        df.index, pd.MultiIndex
    ), "The DataFrame index is not a MultiIndex"


def test_read_csv_custom_separator():
    df = read_csv_custom_separator(SEMICOLON_CSV_PATH, separator=";", decimal=",")
    assert isinstance(df, pd.DataFrame), "The returned object is not a pandas DataFrame"
    assert not df.empty, "The DataFrame is empty"
    assert (
        df["Stars"].dtype == float or df["Stars"].dtype == "float64"
    ), "'Stars' column is not of type float"
