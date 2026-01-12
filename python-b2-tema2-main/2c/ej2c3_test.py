from pathlib import Path
import pandas as pd
import pytest
from ej2c3 import (
    read_csv_basic,
    stack_dataframe,
    unstack_dataframe,
    pivot_dataframe,
    melt_dataframe,
    transpose_dataframe,
)


@pytest.fixture
def products_dataframe():
    current_dir = Path(__file__).parent
    FILE_PATH = current_dir / "data/products.csv"
    return read_csv_basic(FILE_PATH)


def test_read_csv_basic(products_dataframe):
    assert (
        not products_dataframe.empty
    ), "The DataFrame loaded from CSV should not be empty"


def test_stack_dataframe(products_dataframe):
    df_stacked = stack_dataframe(products_dataframe)
    assert isinstance(
        df_stacked, pd.Series
    ), "Stacked DataFrame should be of type 'Series'"


def test_unstack_dataframe(products_dataframe):
    df_stacked = stack_dataframe(products_dataframe)
    df_unstacked = unstack_dataframe(df_stacked)
    assert isinstance(
        df_unstacked, pd.DataFrame
    ), "Unstacked DataFrame should be of type 'DataFrame'"


def test_pivot_dataframe(products_dataframe):
    df_pivoted = pivot_dataframe(products_dataframe)
    assert isinstance(
        df_pivoted, pd.DataFrame
    ), "Pivoted DataFrame should be of type 'DataFrame'"


def test_melt_dataframe(products_dataframe):
    df_melted = melt_dataframe(products_dataframe)
    assert isinstance(
        df_melted, pd.DataFrame
    ), "Melted DataFrame should be of type 'DataFrame'"


def test_transpose_dataframe(products_dataframe):
    df_transposed = transpose_dataframe(products_dataframe)
    assert isinstance(
        df_transposed, pd.DataFrame
    ), "Transposed DataFrame should be of type 'DataFrame'"
