import numpy as np
from ej2a5 import linear_regression_and_interpolation


# Test para verificar los resultados de la regresión lineal
def test_linear_regression_results():
    data_x = np.linspace(0, 10, 100)
    data_y = 3 * data_x + 2 + np.random.normal(0, 0.5, 100)
    results = linear_regression_and_interpolation(data_x, data_y)

    # Asegurarse de que los resultados contengan los componentes esperados
    assert "linear_regression" in results
    assert "interpolated_data" in results

    # Verificar si la pendiente y la intersección están en un rango esperado
    assert 2.5 < results["linear_regression"]["slope"] < 3.5
    assert 1.5 < results["linear_regression"]["intercept"] < 2.5


# Test para verificar la longitud de los datos interpolados
def test_interpolated_data_length():
    data_x = np.linspace(0, 10, 100)
    data_y = 3 * data_x + 2 + np.random.normal(0, 0.5, 100)
    results = linear_regression_and_interpolation(data_x, data_y)

    assert len(results["interpolated_data"]) == len(data_x)
