from pathlib import Path
import pytest
from ej2f3 import df_to_json, df_to_csv, df_to_excel
import pandas as pd
import os

current_dir = Path(__file__).parent
data_path = current_dir / "data/sales.csv"
json_path = current_dir / "data/df_to_json_sales.json"
csv_path = current_dir / "data/df_to_csv_sales.csv"
excel_path = current_dir / "data/df_to_excel_sales.xlsx"


@pytest.fixture
def sales_df():
    return pd.read_csv(data_path)


def test_df_to_json(sales_df):
    _, params = df_to_json(sales_df, json_path)
    assert os.path.exists(json_path), "JSON file should be created."
    assert (
        "orient" in params and params["orient"] == "records"
    ), "Orient parameter should be 'records'."
    assert (
        "lines" in params and params["lines"] is True
    ), "Lines parameter should be True."
    os.remove(json_path)


def test_df_to_csv(sales_df):
    _, params = df_to_csv(sales_df, csv_path)
    assert os.path.exists(csv_path), "CSV file should be created."
    assert (
        "sep" in params and params["sep"] == ";"
    ), "Separator parameter should be ';'."
    assert (
        "header" in params and params["header"] is None
    ), "Header parameter should be None."
    assert (
        "encoding" in params and params["encoding"] == "utf-8"
    ), "Encoding parameter should be 'utf-8'."
    os.remove(csv_path)


def test_df_to_excel(sales_df):
    _, params = df_to_excel(sales_df, excel_path)
    assert os.path.exists(excel_path), "Excel file should be created."
    assert (
        "sheet_name" in params and params["sheet_name"] == "Pandas to Excel"
    ), "Sheet name parameter should be 'Pandas to Excel'."
    os.remove(excel_path)
