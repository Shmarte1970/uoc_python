from pathlib import Path
import pytest
from sklearn.svm import SVC
from ej2d4 import (
    prepare_data,
    train_svm_classifier,
    perform_svm_classification,
    predict_species,
    target_names,
)


@pytest.fixture
def iris_dataset_path():
    current_dir = Path(__file__).parent
    return current_dir / "data/iris_dataset.csv"


@pytest.fixture
def trained_classifier(iris_dataset_path):
    X_train, X_test, y_train, y_test = prepare_data(iris_dataset_path)
    clf = train_svm_classifier(X_train, y_train)
    return clf, X_test, y_test


def test_prepare_data(iris_dataset_path):
    X_train, X_test, y_train, y_test = prepare_data(iris_dataset_path)
    # Asegurarse de que los datos estén divididos correctamente
    assert len(X_train) > 0 and len(X_test) > 0
    assert len(y_train) > 0 and len(y_test) > 0
    # Comprobar que la proporción de división es aproximadamente 80/20
    assert len(X_train) / (len(X_train) + len(X_test)) == pytest.approx(
        0.8, 0.05
    ), "The training set should be around 80% of the total data"


def test_train_svm_classifier(iris_dataset_path):
    X_train, _, y_train, _ = prepare_data(iris_dataset_path)
    clf = train_svm_classifier(X_train, y_train)
    # Comprobar que el clasificador es una instancia de SVC
    assert isinstance(clf, SVC), "The classifier should be an instance of SVC"


def test_perform_svm_classification(trained_classifier):
    clf, X_test, y_test = trained_classifier
    accuracy, report = perform_svm_classification(X_test, y_test, clf)
    assert 0 <= accuracy <= 1, "The accuracy should be in the range [0, 1]"


def test_predict_species(trained_classifier):
    clf, X_test, y_test = trained_classifier
    feature_names = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]
    prediction = predict_species(clf, [5.1, 3.5, 1.4, 0.2], feature_names)
    assert (
        prediction in target_names.values()
    ), "The prediction should be one of the target names"
