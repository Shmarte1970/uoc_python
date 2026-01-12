from pathlib import Path
import pytest
import pandas as pd
from sklearn.linear_model import LinearRegression
from ej2d5 import (
    prepare_data_for_regression,
    perform_linear_regression,
    evaluate_regression_model,
)


@pytest.fixture
def load_housing_data():
    current_dir = Path(__file__).parent
    file_path = current_dir / "data/housing.csv"
    data = pd.read_csv(file_path, skiprows=14)
    return data


@pytest.fixture
def prepared_data(load_housing_data):
    X_train, X_test, y_train, y_test = prepare_data_for_regression(load_housing_data)
    return X_train, X_test, y_train, y_test


def test_prepare_data_for_regression(prepared_data):
    X_train, X_test, y_train, y_test = prepared_data
    assert not X_train.empty and not X_test.empty
    assert not y_train.empty and not y_test.empty
    assert len(X_train) / (len(X_train) + len(X_test)) == pytest.approx(0.8, abs=1e-2)


def test_perform_linear_regression(prepared_data):
    X_train, _, y_train, _ = prepared_data
    model = perform_linear_regression(X_train, y_train)
    assert isinstance(model, LinearRegression)


def test_evaluate_regression_model(prepared_data):
    X_train, X_test, y_train, y_test = prepared_data
    model = perform_linear_regression(X_train, y_train)
    r_squared, rmse = evaluate_regression_model(model, X_test, y_test)
    assert isinstance(r_squared, float) and isinstance(rmse, float)
