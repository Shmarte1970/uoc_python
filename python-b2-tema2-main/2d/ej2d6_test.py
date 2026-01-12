from pathlib import Path
import pytest
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from ej2d6 import (
    prepare_data_for_regression,
    perform_random_forest_regression,
    evaluate_regression_model,
)


@pytest.fixture
def sample_data_path():
    current_dir = Path(__file__).parent
    file_path = current_dir / "data/housing.csv"
    return file_path


@pytest.fixture
def prepared_data(sample_data_path):
    X_train, X_test, y_train, y_test = prepare_data_for_regression(sample_data_path)
    return X_train, X_test, y_train, y_test


def test_prepare_data_for_regression(prepared_data):
    X_train, X_test, y_train, y_test = prepared_data
    assert (
        not X_train.empty and not X_test.empty
    ), "The training and test sets should not be empty"
    assert (
        not y_train.empty and not y_test.empty
    ), "The training and test targets should not be empty"
    assert len(X_train) > len(X_test) and len(y_train) > len(
        y_test
    ), "The training set should be larger than the test set"


def test_perform_random_forest_regression(prepared_data):
    X_train, _, y_train, _ = prepared_data
    model = perform_random_forest_regression(X_train, y_train)
    assert isinstance(
        model, RandomForestRegressor
    ), "The model should be an instance of RandomForestRegressor"
    assert hasattr(
        model, "feature_importances_"
    ), "The model should have a 'feature_importances_' attribute"


def test_evaluate_regression_model(prepared_data):
    X_train, X_test, y_train, y_test = prepared_data
    model = perform_random_forest_regression(X_train, y_train)
    r_squared, rmse = evaluate_regression_model(model, X_test, y_test)
    assert isinstance(r_squared, float) and isinstance(
        rmse, float
    ), "The R^2 and RMSE should be floats"
    assert -1 <= r_squared <= 1, "The R^2 should be in the range [-1, 1]"
    assert rmse >= 0, "The RMSE should be a positive number"
