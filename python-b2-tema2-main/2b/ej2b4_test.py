import pandas as pd
import pytest
from pathlib import Path

from ej2b4 import read_excel_sheet, read_excel_custom_sheet


@pytest.fixture
def excel_file_path():
    current_dir = Path(__file__).parent
    return current_dir / "data/ej2b4/ramen-ratings.xlsx"


# Test for read_excel_sheet function
def test_read_excel_sheet(excel_file_path):
    df = read_excel_sheet(excel_file_path)
    assert isinstance(
        df, pd.DataFrame
    ), "The returned object should be a Pandas DataFrame."
    assert not df.empty, "The DataFrame should not be empty."
    # Assuming you know the number of rows/columns that the DataFrame should have
    assert df.shape[0] > 0, "The DataFrame should have more than 0 rows."
    assert df.shape[1] > 0, "The DataFrame should have more than 0 columns."


# Test for read_excel_custom_sheet function
def test_read_excel_custom_sheet(excel_file_path):
    df = read_excel_custom_sheet(excel_file_path)
    assert isinstance(
        df, pd.DataFrame
    ), "The returned object should be a Pandas DataFrame."
    assert not df.empty, "The DataFrame should not be empty."
    # Verify that the first columns do not contain 'Unnamed' which would imply empty columns
    assert not df.columns.str.contains(
        "Unnamed"
    ).any(), "Columns should not contain 'Unnamed' which implies empty columns."
    # Verify that the expected columns and rows are present
    expected_columns = [
        "Brand",
        "Country",
        "Review #",
        "Stars",
        "Style",
        "Top Ten",
        "Variety",
    ]
    for col in expected_columns:
        assert col in df.columns, f"The expected column '{col}' is missing."
    # Verify that the last 4 rows have been skipped if you know the total number of rows
    expected_row_count = 2580
    assert len(df) == expected_row_count, (
        f"The DataFrame should have the expected number of rows, after skipping the"
        f"footer."
    )
