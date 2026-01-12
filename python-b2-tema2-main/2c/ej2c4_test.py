import pandas as pd
import pytest
from ej2c4 import (
    group_and_aggregate,
    standardize_column_by_group,
)  # Ajusta el import según el nombre de tu archivo


@pytest.fixture
def products_df():
    data = {
        "Category": [
            "Electronics",
            "Electronics",
            "Clothing",
            "Clothing",
            "Electronics",
        ],
        "Brand": ["BrandA", "BrandA", "BrandB", "BrandB", "BrandA"],
        "Price": [120, 150, 50, 60, 200],
        "Rating": [4.5, 4.0, 3.5, 4.0, 5.0],
    }
    return pd.DataFrame(data)


def test_group_and_aggregate(products_df):
    group_columns = ["Category"]
    agg_dict = {"Price": ["mean", "sum"], "Rating": ["mean"]}
    result = group_and_aggregate(products_df, group_columns, agg_dict)

    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame."
    assert not result.empty, "The result DataFrame should not be empty."
    assert ("Price", "mean") in result.columns, "The result should include mean price."
    assert ("Price", "sum") in result.columns, "The result should include sum price."
    assert (
        "Rating",
        "mean",
    ) in result.columns, "The result should include mean rating."
    expected_price_mean_electronics = (120 + 150 + 200) / 3
    expected_price_sum_electronics = 120 + 150 + 200
    expected_rating_mean_electronics = (4.5 + 4.0 + 5.0) / 3
    assert (
        result.loc["Electronics", ("Price", "mean")] == expected_price_mean_electronics
    ), "The mean price for Electronics is incorrect."
    assert (
        result.loc["Electronics", ("Price", "sum")] == expected_price_sum_electronics
    ), "The sum price for Electronics is incorrect."
    assert result.loc["Electronics", ("Rating", "mean")] == pytest.approx(
        expected_rating_mean_electronics
    ), "The mean rating for Electronics is incorrect."


def test_standardize_column_by_group(products_df):
    group_columns = ["Category", "Brand"]
    column_to_standardize = "Rating"
    df_result = standardize_column_by_group(
        products_df.copy(), group_columns, column_to_standardize
    )

    standardized_col_name = f"{column_to_standardize}_Standardized"
    assert (
        standardized_col_name in df_result.columns
    ), f"The column '{standardized_col_name}' should be added to the DataFrame."
    assert pd.api.types.is_float_dtype(
        df_result[standardized_col_name]
    ), f"The column '{standardized_col_name}' should be of float type."
    assert (
        not df_result[standardized_col_name].isnull().all()
    ), f"The column '{standardized_col_name}' should not be all NaN."
    assert (
        df_result[standardized_col_name].min() < 0
    ), "Standardized ratings should include negative values."
    assert (
        df_result[standardized_col_name].max() > 0
    ), "Standardized ratings should include positive values."
