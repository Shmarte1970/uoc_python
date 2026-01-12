import pytest
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from ej2e3 import data_processing, pairplot_graphic


def test_data_processing():
    iris = load_iris()
    df_iris = data_processing(
        iris.data, iris.feature_names, iris.target, iris.target_names
    )
    assert isinstance(df_iris, pd.DataFrame), "The result should be a pandas DataFrame"
    expected_columns = list(iris.feature_names) + ["species"]
    assert all(
        column in df_iris.columns for column in expected_columns
    ), "DataFrame should contain the expected columns"
    assert len(df_iris) == len(
        iris.data
    ), "DataFrame should have the same number of rows as the input data"


def test_pairplot_graphic_with_full_dataframe():
    iris = load_iris()
    df_iris = data_processing(
        iris.data, iris.feature_names, iris.target, iris.target_names
    )
    viz_params = {
        "hue": "species",
        "diag_kind": "kde",
        "kind": "scatter",
        "palette": "husl",
        "corner": True,
    }
    plot = pairplot_graphic(df_iris, **viz_params)
    assert isinstance(
        plot, sns.PairGrid
    ), "The function should return a seaborn PairGrid object"


def test_pairplot_graphic_with_specific_columns():
    iris = load_iris()
    df_iris = data_processing(
        iris.data, iris.feature_names, iris.target, iris.target_names
    )
    viz_params = {
        "hue": "species",
        "diag_kind": "kde",
        "kind": "scatter",
        "palette": "husl",
        "corner": True,
    }
    columns_to_visualize = ["sepal length (cm)", "sepal width (cm)"]
    plot = pairplot_graphic(df_iris, columns=columns_to_visualize, **viz_params)
    assert isinstance(
        plot, sns.PairGrid
    ), "The function should return a seaborn PairGrid object even with specific columns"
