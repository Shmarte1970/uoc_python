import numpy as np

from ej2a6 import gaussian_fit_and_integration


def test_gaussian_fit_results():
    data_x = np.linspace(-5, 5, 100)
    # Generar datos con una curva gaussiana conocida
    data_y = 3 * np.exp(-((data_x - 1) ** 2) / (2 * 1.5**2)) + np.random.normal(
        0, 0.2, 100
    )
    params, _ = gaussian_fit_and_integration(data_x, data_y)

    # put asserts in english
    assert 2 < params[0] < 4, "Ampitude out of expected range"
    assert 0 < params[1] < 2, "Mean out of expected range"
    assert 1 < params[2] < 2, "Stddev out of expected range"


# Test para verificar la integración de la curva gaussiana
def test_gaussian_integration():
    data_x = np.linspace(-5, 5, 100)
    data_y = 3 * np.exp(-((data_x - 1) ** 2) / (2 * 1.5**2)) + np.random.normal(
        0, 0.2, 100
    )
    params, integral = gaussian_fit_and_integration(data_x, data_y)

    expected_integral = params[0] * params[2] * np.sqrt(2 * np.pi)
    assert np.isclose(
        integral, expected_integral, atol=1
    ), "Integral out of expected range"
