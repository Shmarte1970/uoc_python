from pathlib import Path
import pytest
import pandas as pd
from sklearn.decomposition import PCA
from ej2c6 import prepare_data_for_pca, perform_pca


@pytest.fixture
def sample_data_path():
    current_dir = Path(__file__).parent
    FILE_PATH = current_dir / "data/housing.csv"
    return FILE_PATH


def test_prepare_data_for_pca(sample_data_path):
    data = prepare_data_for_pca(sample_data_path)
    assert not data.empty, "The data should not be empty"
    assert (
        "MEDV" not in data.columns
    ), "The target variable should not be included in the data"


def test_perform_pca(sample_data_path):
    data = prepare_data_for_pca(sample_data_path)
    pca = perform_pca(data, n_components=4)
    assert isinstance(pca, PCA), "The returned object should be an instance of PCA"
    assert pca.n_components_ == 4, "The number of principal components should be 4"
