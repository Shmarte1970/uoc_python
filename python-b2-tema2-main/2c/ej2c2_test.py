from pathlib import Path
import pandas as pd
import pytest
import numpy as np
from pandas.testing import assert_series_equal
from ej2c2 import read_csv_basic, custom_dataframe_describe, pandas_dataframe_describe


@pytest.fixture(scope="module")
def load_dataframe():
    current_dir = Path(__file__).parent
    FILE_PATH = current_dir / "data/grades.csv"
    return read_csv_basic(FILE_PATH)


def test_read_csv_basic(load_dataframe):
    assert not load_dataframe.empty, "The DataFrame should not be empty."
    expected_columns = ["Maths", "English", "Science"]
    assert all(
        column in load_dataframe.columns for column in expected_columns
    ), "DataFrame should have expected columns."


def test_custom_dataframe_describe(load_dataframe):
    result = custom_dataframe_describe(load_dataframe)
    expected_stats = [
        "count",
        "mean",
        "median",
        "std",
        "min",
        "25%",
        "50%",
        "75%",
        "max",
    ]
    assert all(
        stat in result.index for stat in expected_stats
    ), "Custom describe should include all expected statistics."
    expected_mean_math = 48.216354
    assert np.isclose(
        result.loc["mean", "Maths"], expected_mean_math
    ), f"Expected mean for Maths should be {expected_mean_math}, got {result.loc['mean', 'Maths']}"
    expected_means = pd.Series(
        {
            "Hindi": 52.124361,
            "English": 49.862010,
            "Science": 48.686542,
            "Maths": 48.216354,
            "History": 49.240204,
            "Geography": 49.603066,
        }
    )
    assert_series_equal(
        result.loc["mean"],
        expected_means,
        check_names=False,
        check_exact=False,
        rtol=1e-5,
    ),


def test_pandas_dataframe_describe(load_dataframe):
    result = pandas_dataframe_describe(load_dataframe)
    expected_stats = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
    assert all(
        stat in result.index for stat in expected_stats
    ), "Pandas describe should include all default statistics."
