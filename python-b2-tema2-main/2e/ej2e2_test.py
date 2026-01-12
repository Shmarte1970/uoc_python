import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from ej2e2 import (
    create_meshgrid,
    plot_decision_boundaries,
    plot_confusion_matrix,
    train_and_visualize,
)


def test_create_meshgrid():
    X = np.array([[1, 2], [3, 4], [5, 6]])
    xx1, xx2 = create_meshgrid(X)
    assert xx1.shape == xx2.shape, "Meshgrid arrays should have the same shape"
    assert (
        xx1.min() < X[:, 0].min()
    ), "Meshgrid x1 min should be less than X[:, 0].min()"
    assert (
        xx2.min() < X[:, 1].min()
    ), "Meshgrid x2 min should be less than X[:, 1].min()"


def test_plot_decision_boundaries():
    iris = load_iris()
    X = iris.data[:, :2]
    y = iris.target
    fig, ax = plt.subplots()
    classifier = KNeighborsClassifier(n_neighbors=3)
    classifier.fit(X, y)
    ax = plot_decision_boundaries(ax, X, y, classifier)
    assert ax, "plot_decision_boundaries should return a matplotlib axis"
    assert (
        len(ax.collections) > 0
    ), "plot_decision_boundaries should add collections to the axis"


def test_plot_confusion_matrix():
    fig, ax = plt.subplots()
    y_true = np.array([0, 1, 2, 2, 1])
    y_pred = np.array([0, 1, 2, 1, 1])
    classes = ["class 0", "class 1", "class 2"]
    ax = plot_confusion_matrix(ax, y_true, y_pred, classes)
    assert ax, "plot_confusion_matrix should return a matplotlib axis"
    assert len(ax.texts) > 0, "Confusion matrix should contain text annotations"
    assert (
        ax.get_title() == "Confusion Matrix"
    ), "plot_confusion_matrix should set the correct title"


def test_train_and_visualize():
    iris = load_iris()
    X = iris.data[:, :2]
    y = iris.target
    X_train, X_test, y_train, y_test, classifier = train_and_visualize(X, y)
    assert len(X_train) > 0, "X_train should not be empty"
    assert len(X_test) > 0, "X_test should not be empty"
    assert len(y_train) > 0, "y_train should not be empty"
    assert len(y_test) > 0, "y_test should not be empty"
    assert len(np.unique(classifier.predict(X_test))) <= len(
        np.unique(y)
    ), "Predicted classes should not exceed the actual classes"
