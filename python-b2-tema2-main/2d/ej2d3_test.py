from pathlib import Path
import pytest
import pandas as pd
from ej2d3 import perform_linear_regression, plot_regression_line


@pytest.fixture
def housing_data():
    current_dir = Path(__file__).parent
    data = pd.read_csv(current_dir / "data/housing.csv", skiprows=14)
    return data


def test_perform_linear_regression(housing_data):
    slope, intercept, r_value, p_value, std_err = perform_linear_regression(
        housing_data, "RM", "MEDV"
    )
    assert isinstance(slope, float), "The slope should be a float"
    assert isinstance(intercept, float), "The intercept should be a float"
    assert r_value**2 <= 1, "The r squared value should be less than or equal to 1"
    assert 0 <= p_value <= 1, "The p value should be in the range [0, 1]"
    assert isinstance(std_err, float), "The standard error should be a float"


def test_plot_regression_line(housing_data):
    slope = 5  # Use fictitious values for the slope and the intercept
    intercept = -1
    _, ax = plot_regression_line(
        housing_data, "RM", "MEDV", slope, intercept, return_fig_ax_test=True
    )
    assert (
        ax.get_title() == "Linear Regression between RM and MEDV"
    ), "The chart title is not correct"
    assert ax.get_xlabel() == "RM", "The X axis label is not correct"
    assert ax.get_ylabel() == "MEDV", "The Y axis label is not correct"
