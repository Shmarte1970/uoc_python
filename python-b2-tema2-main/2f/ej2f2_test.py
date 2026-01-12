import pytest
from sklearn.datasets import load_wine
import os
import tempfile
from ej2f2 import (
    train_model,
    save_model,
    load_model_and_predict,
    plot_feature_importance,
)


@pytest.fixture(scope="module")
def wine_data():
    return load_wine(return_X_y=True)


@pytest.fixture(scope="module")
def trained_model(wine_data):
    X, y = wine_data
    model, X_test, y_test = train_model(X, y)
    return model, X_test, y_test


def test_train_model(trained_model):
    model, X_test, y_test = trained_model
    assert model is not None, "Model should be successfully created."
    assert len(X_test) > 0, "X_test should contain test samples."
    assert len(y_test) > 0, "y_test should contain test labels."


def test_save_model(trained_model):
    model, _, _ = trained_model
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filepath = tmp.name
    result = save_model(model, filepath)
    assert result is True, "save_model should return True indicating success."
    assert os.path.exists(filepath), "Model file should be created."
    os.remove(filepath)


def test_load_model_and_predict(trained_model):
    model, X_test, _ = trained_model
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filepath = tmp.name
    save_model(model, filepath)

    predictions = load_model_and_predict(filepath, X_test)
    assert predictions is not None, "load_model_and_predict should return predictions."
    assert len(predictions) == len(
        X_test
    ), "Number of predictions should match number of test samples."
    os.remove(filepath)


def test_plot_feature_importance(trained_model):
    model, _, _ = trained_model
    feature_names = load_wine().feature_names
    fig = plot_feature_importance(model, feature_names)
    assert (
        fig is not None
    ), "plot_feature_importance should return a matplotlib Figure object."
