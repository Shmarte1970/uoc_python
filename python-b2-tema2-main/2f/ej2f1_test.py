import pytest
from sklearn.datasets import load_wine
import pandas as pd
import os
import tempfile
import matplotlib.pyplot as plt
from ej2f1 import create_histograms, save_img_pickle, load_and_display_figure


@pytest.fixture
def wine_data():
    wine = load_wine()
    df_wine = pd.DataFrame(data=wine.data, columns=wine.feature_names)
    df_wine["target"] = pd.Categorical.from_codes(wine.target, wine.target_names)
    return df_wine


def test_create_histograms(wine_data):
    fig = create_histograms(wine_data, wine_data.columns[:6])
    assert (
        fig is not None
    ), "The figure should not be None, indicating that create_histograms successfully created a figure."
    plt.close(fig)


def test_save_img_pickle(wine_data):
    fig = create_histograms(wine_data, wine_data.columns[:6])
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        filename = tmpfile.name
    os.unlink(filename)

    save_img_pickle(fig, filename)
    assert os.path.isfile(filename), "File should be created by save_img_pickle."

    os.remove(filename)
    plt.close(fig)


def test_load_and_display_figure(wine_data):

    fig = create_histograms(wine_data, wine_data.columns[:6])
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        filename = tmpfile.name
    save_img_pickle(fig, filename)
    plt.close(fig)

    loaded_fig = load_and_display_figure(filename)
    assert (
        loaded_fig is not None
    ), "load_and_display_figure should return a Figure object."

    plt.close(loaded_fig)
    os.remove(filename)
