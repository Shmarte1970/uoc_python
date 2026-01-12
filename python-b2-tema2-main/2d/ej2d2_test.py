from pathlib import Path
import pytest
from ej2d2 import (
    calculate_pearson_correlation,
)  # Asegúrate de reemplazar 'tu_script' con el nombre de tu script


@pytest.fixture
def housing_data_path():
    current_dir = Path(__file__).parent
    return current_dir / "data/housing.csv"


def test_calculate_pearson_correlation_positive(housing_data_path):
    variable_1 = "RM"
    variable_2 = "MEDV"
    correlation, p_value = calculate_pearson_correlation(
        housing_data_path, variable_1, variable_2
    )
    assert (
        correlation > 0
    ), f"A positive correlation was expected between {variable_1} and {variable_2}"
    assert (
        p_value < 0.05
    ), f"The p-value should indicate statistical significance for {variable_1} and {variable_2}"


def test_calculate_pearson_correlation_negative(housing_data_path):
    variable_1 = "LSTAT"
    variable_2 = "MEDV"
    correlation, p_value = calculate_pearson_correlation(
        housing_data_path, variable_1, variable_2
    )
    assert (
        correlation < 0
    ), f"A negative correlation was expected between {variable_1} and {variable_2}"
    assert (
        p_value < 0.05
    ), f"The p-value should indicate statistical significance for {variable_1} and {variable_2}"


def test_calculate_pearson_correlation_no_correlation(housing_data_path):
    variable_1 = "CHAS"
    variable_2 = "RAD"
    correlation, p_value = calculate_pearson_correlation(
        housing_data_path, variable_1, variable_2
    )
    assert (
        -0.1 < correlation < 0.1
    ), f"A correlation close to 0 was expected between {variable_1} and {variable_2}"
    # Note: The p-value may not be significant in this case, which is acceptable given the expected lack of correlation.


def test_calculate_pearson_correlation_invalid_input(housing_data_path):
    variable_1 = "INVALID_VAR1"
    variable_2 = "INVALID_VAR2"
    with pytest.raises(Exception) as excinfo:
        calculate_pearson_correlation(housing_data_path, variable_1, variable_2)
    assert "INVALID_VAR1" in str(
        excinfo.value
    ), f"An exception was expected due to invalid variables {variable_1} and {variable_2}"


# Optional: You might want to add a test for handling missing data or NaN values if applicable
def test_calculate_pearson_correlation_missing_data(housing_data_path):
    variable_1 = "RM"  # Assuming 'RM' might have missing data for the sake of example
    variable_2 = "MEDV"
    correlation, p_value = calculate_pearson_correlation(
        housing_data_path, variable_1, variable_2
    )
    assert (
        correlation is not None
    ), f"Correlation should be calculated even if missing data is present for {variable_1} and {variable_2}"
    assert (
        p_value is not None
    ), f"P-value should be calculated even if missing data is present for {variable_1} and {variable_2}"
