"""
Enunciado:

Explora el análisis avanzado de datos y la aplicación de ajustes no lineales mediante el uso de SciPy. Este ejercicio se
centra en ajustar una función gaussiana a un conjunto de datos usando el módulo scipy.optimize.curve_fit y en calcular
la integral de esta curva con scipy.integrate.quad.

Implementar la función gaussian_fit_and_integration(data_x, data_y) que realice lo siguiente:
    Ajuste de Curva Gaussiana: Utilizar scipy.optimize.curve_fit para ajustar una curva gaussiana a los datos.
    Integración Numérica: Calcular la integral de la curva gaussiana ajustada sobre el rango de data_x utilizando
    scipy.integrate.quad.

Además, implementar la función plot_gaussian_fit(data_x, data_y, gaussian_params) para visualizar los datos originales
y la curva gaussiana ajustada.

Parámetros:
    data_x (List[float]): Lista de valores en el eje x.
    data_y (List[float]): Lista de valores en el eje y correspondientes a data_x.
    gaussian_params (Tuple[float]): Parámetros (amplitud, centro, ancho) de la curva gaussiana ajustada.

Ejemplo:
    Entrada:
        data_x = np.linspace(-5, 5, 100)
        data_y = 3 * np.exp(-(data_x - 1)**2 / (2 * 1.5**2)) + np.random.normal(0, 0.2, 100)
    Ejecución:
        gaussian_params, integral = gaussian_fit_and_integration(data_x, data_y)
        plot_gaussian_fit(data_x, data_y, gaussian_params)
    Salida:
        Un gráfico mostrando los datos originales y la curva gaussiana ajustada.
        La integral de la curva gaussiana ajustada.
"""

from scipy import optimize, integrate
import numpy as np
import matplotlib.pyplot as plt
import typing as t


def gaussian(x: float, amplitude: float, mean: float, stddev: float) -> float:
    return amplitude * np.exp(-((x - mean) ** 2) / (2 * stddev**2))

def gaussian_fit_and_integration(
    data_x: t.List[float], data_y: t.List[float]
) -> t.Tuple[t.Tuple[float], float]:

    x = np.array(data_x)
    y = np.array(data_y)

    
    initial_guess = [
        np.max(y),          # amplitude
        x[np.argmax(y)],    # mean
        np.std(x),          # stddev
    ]

    
    params, _ = optimize.curve_fit(gaussian, x, y, p0=initial_guess)

    amplitude, mean, stddev = params

    
    integral, _ = integrate.quad(
        gaussian, x.min(), x.max(), args=(amplitude, mean, stddev)
    )

    return (amplitude, mean, stddev), integral


def plot_gaussian_fit(
    data_x: t.List[float], data_y: t.List[float], gaussian_params: t.Tuple[float]
):
    x = np.array(data_x)
    y = np.array(data_y)

    y_fit = gaussian(x, *gaussian_params)

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, label="Original Data", alpha=0.6)
    plt.plot(x, y_fit, label="Gaussian Fit", linewidth=2)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Gaussian Fit to Data")
    plt.legend()
    plt.grid(True)
    plt.show()


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
data_x = np.linspace(-5, 5, 100)
data_y = 3 * np.exp(-(data_x - 1) ** 2 / (2 * 1.5 ** 2)) + np.random.normal(0, 0.2, 100)
gaussian_params, integral = gaussian_fit_and_integration(data_x, data_y)
print("Integral de la curva gaussiana ajustada:", integral)
plot_gaussian_fit(data_x, data_y, gaussian_params)
