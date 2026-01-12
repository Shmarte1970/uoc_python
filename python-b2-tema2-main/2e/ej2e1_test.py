from pathlib import Path
import pytest
import pandas as pd
import matplotlib.pyplot as plt
from ej2e1 import plot_area_graph, plot_scatter_graph


@pytest.fixture
def sample_dataframe():
    current_dir = Path(__file__).parent
    path_csv = current_dir / "data/iris_dataset.csv"
    df = pd.read_csv(path_csv)
    return df


def test_plot_area_graph(sample_dataframe):
    fig, ax = plt.subplots()
    returned_fig, returned_ax = plot_area_graph(
        sample_dataframe, "petal length (cm)", ax=ax
    )
    assert (
        len(returned_ax.get_legend().get_texts()) > 0
    ), "Legend was not created properly"
    assert returned_ax.get_xlabel() == "Index", "X-axis title is incorrect"
    assert returned_ax.get_ylabel() == "petal length (cm)", "Y-axis title is incorrect"
    assert (
        returned_ax.get_title() == "Area Graph of petal length (cm)"
    ), "Graph title is incorrect"


def test_plot_scatter_graph(sample_dataframe):
    fig, ax = plt.subplots()
    returned_fig, returned_ax = plot_scatter_graph(
        sample_dataframe, "sepal length (cm)", "sepal width (cm)", ax=ax
    )
    assert (
        len(returned_ax.get_legend().get_texts()) > 0
    ), "Legend was not created properly"
    assert returned_ax.get_xlabel() == "sepal length (cm)", "X-axis title is incorrect"
    assert returned_ax.get_ylabel() == "sepal width (cm)", "Y-axis title is incorrect"
    assert (
        returned_ax.get_title()
        == "Scatter Plot of sepal length (cm) vs sepal width (cm)"
    ), "Graph title is incorrect"
