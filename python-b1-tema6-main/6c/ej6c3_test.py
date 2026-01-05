import pandas as pd
from ej6c3 import read_parquet_file, calculate_amount_quanity
import os, pathlib


def test_read_parquet_file():
    # Checking how pytest was called lo locate the file
    launch_path = pathlib.Path.cwd()
    path = "files" + os.sep + "sales_products_2020_08.parquet"
    if str(launch_path).split(os.sep)[-1].startswith("python-b1"):
        path = "6c" + os.sep + path

    df_result = read_parquet_file(path)
    expected_values_first_row = [
        "2020 Summer Vintage Flamingo Print  Pajamas Set Casual Loose T Shirt Top And Elastic Shorts Women Sleepwear Night Wear Loungewear Sets",
        16.0,
        14,
        100,
        3.76,
        54,
        "5e9ae51d43d6a96e303acdb0",
        "2020-08",
    ]
    assert (
        df_result.iloc[0].tolist() == expected_values_first_row
    ), "The values in the first row of the DataFrame do not match the expected values."


def test_calculate_amount_quantity():
    df_test = pd.DataFrame({"price": [10, 20, 30], "units_sold": [2, 4, 6]})

    df_expected = pd.DataFrame(
        {"price": [10, 20, 30], "units_sold": [2, 4, 6], "amount": [20, 80, 180]}
    )

    df_result = calculate_amount_quanity(df_test)
    try:
        pd.testing.assert_frame_equal(df_result, df_expected)
    except AssertionError:
        print("The result DataFrame is not equal to the expected DataFrame.")
        print(f"Expected DataFrame:\n{df_expected}")
        print(f"Result DataFrame:\n{df_result}")
        raise
