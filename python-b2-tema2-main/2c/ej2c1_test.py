import pandas as pd
import pytest
from pathlib import Path
from ej2c1 import select_rows_and_columns, select_rows_with_conditions


@pytest.fixture(scope="module")
def df_grades():
    current_dir = Path(__file__).parent
    FILE_PATH = current_dir / "data/grades.csv"
    return pd.read_csv(FILE_PATH)


def test_select_rows_and_columns_by_name(df_grades):
    result = select_rows_and_columns(df_grades, ["Name", "Maths", "History"])
    expected_columns = ["Name", "Maths", "History"]
    assert (
        list(result.columns) == expected_columns
    ), "Column names do not match the expected columns"


def test_select_rows_and_columns_by_index(df_grades):
    result = select_rows_and_columns(df_grades, [0, 1, 3])
    expected_columns = df_grades.columns[[0, 1, 3]].tolist()
    assert (
        list(result.columns) == expected_columns
    ), "Column index do not match the expected columns"


def test_select_rows_with_conditions_single(df_grades):
    result = select_rows_with_conditions(df_grades, "English > 50")
    assert not result.empty, "The DataFrame should not be empty"
    assert all(result["English"] > 50), "Not all rows meet the condition"


def test_select_rows_with_conditions_multiple(df_grades):
    conditions = ["English > 50", "Maths >= 60", "Geography > 55"]
    result = select_rows_with_conditions(df_grades, conditions)
    assert not result.empty, "The DataFrame should not be empty"
    assert (
        all(result["English"] > 50)
        and all(result["Maths"] >= 60)
        and all(result["Geography"] > 55)
    ), "Not all rows meet the conditions"
