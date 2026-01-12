from ej2a3 import create_and_modify_meshgrid

import numpy as np


def test_create_and_modify_meshgrid():
    start, end, step = -5, 5, 1
    X, Y = create_and_modify_meshgrid(start, end, step)

    # Verificar dimensiones de las matrices X e Y
    assert X.shape == (11, 11)
    assert Y.shape == (11, 11)

    # Verificar si la cuadrícula se ha generado correctamente
    expected_x = np.arange(start, end + 1, step)
    expected_y = np.arange(start, end + 1, step)
    assert np.all(X[1, :] == expected_x)  # Verificar una fila de X
    assert np.all(Y[:, 1] == expected_y)  # Verificar una columna de Y

    # Verificar la modificación realizada en la fila 0 de X
    assert np.all(X[0, :] == 99)
