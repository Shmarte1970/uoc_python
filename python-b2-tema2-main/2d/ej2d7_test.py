import pytest
import numpy as np
from pathlib import Path
from ej2d7 import (
    prepare_data_for_clustering,
    perform_kmeans_clustering,
    visualize_clusters,
)


@pytest.fixture
def german_credit_data_path():
    current_dir = Path(__file__).parent
    file_path = current_dir / "data/german_credit_data.csv"
    return file_path


def test_prepare_data_for_clustering(german_credit_data_path):
    data_scaled = prepare_data_for_clustering(german_credit_data_path)        
    std_mean = data_scaled.mean(axis=0)   
    
    expected_value = 0
    tolerance = 1e-6
    assert np.all(np.abs(std_mean - expected_value) <= tolerance), \
               "The data should be centered around 0"
    
    std_values = data_scaled.std(axis=0)   
    
    expected_value = 1.0
    tolerance = 1e-6
    assert np.all(np.abs(std_values - expected_value) <= tolerance), \
               "The data should have a standard deviation of 1"


def test_perform_kmeans_clustering(german_credit_data_path):
    data_scaled = prepare_data_for_clustering(german_credit_data_path)
    n_clusters = 5
    labels = perform_kmeans_clustering(data_scaled, n_clusters)
    assert len(labels) > 0, "The labels should not be empty"
    assert (
        len(set(labels)) == n_clusters
    ), "The number of unique labels should match the number of clusters"


def test_visualize_clusters(german_credit_data_path):
    data_scaled = prepare_data_for_clustering(german_credit_data_path)
    n_clusters = 5
    labels = perform_kmeans_clustering(data_scaled, n_clusters)
    data_reduced, fig, ax = visualize_clusters(data_scaled, labels, True)
    assert data_reduced.shape[1] == 2, "The data should be reduced to 2 dimensions"
