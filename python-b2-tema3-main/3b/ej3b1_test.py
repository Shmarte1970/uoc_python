from ej3b1 import (
    df_to_json,
    df_to_csv,
    df_to_excel,
)
from pathlib import Path
import pandas as pd
import os

# Datos de prueba
df_test = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

path = Path(__file__).parent
path_output = path / "data/output"
path_output.mkdir(parents=True, exist_ok=True)
test_csv_filename = "test_data.csv"
test_json_filename = "test_data.json"
test_excel_filename = "test_data.xlsx"


def test_df_to_json():
    (df_from_json, params_json), execution_time_json = df_to_json(
        df_test, test_json_filename, path_output
    )
    assert os.path.exists(path_output / test_json_filename), "The JSON file was not created."
    assert not df_from_json.empty, "The DataFrame loaded from JSON is empty."
    os.remove(path_output / test_json_filename)


def test_df_to_csv():
    (df_from_csv, params_csv), execution_time_csv = df_to_csv(
        df_test, test_csv_filename, path_output
    )
    assert os.path.exists(path_output / test_csv_filename), "The CSV file was not created."
    assert not df_from_csv.empty, "The DataFrame loaded from CSV is empty."
    os.remove(path_output / test_csv_filename)


def test_df_to_excel():
    (df_from_excel, params_excel), execution_time_excel = df_to_excel(
        df_test, test_excel_filename, path_output
    )
    assert os.path.exists(path_output / test_excel_filename), "The Excel file was not created."
    assert not df_from_excel.empty, "The DataFrame loaded from Excel is empty."
    os.remove(path_output / test_excel_filename)


def test_json_vs_excel_execution_time():
    _, execution_time_json = df_to_json(df_test, test_json_filename, path_output)
    _, execution_time_csv = df_to_csv(df_test, test_json_filename, path_output)
    _, execution_time_excel = df_to_excel(df_test, test_excel_filename, path_output)
    assert (
        execution_time_json < execution_time_excel
    ), "JSON export should be faster than Excel export."
    assert (
        execution_time_csv < execution_time_excel
    ), "CSV export should be faster than Excel export."
    os.remove(path_output / test_json_filename)
    os.remove(path_output / test_excel_filename)

test_df_to_json()