from ej2a2 import create_matrices, manipulate_matrices
import numpy as np


def test_create_matrices():
    zeros_matrix, ones_matrix, identity_matrix = create_matrices()

    # Prueba para matriz de ceros
    assert zeros_matrix.shape == (3, 3)
    assert np.all(zeros_matrix == np.zeros((3, 3)))

    # Prueba para matriz de unos
    assert ones_matrix.shape == (2, 4)
    assert np.all(ones_matrix == np.ones((2, 4)))

    # Prueba para matriz identidad
    assert identity_matrix.shape == (4, 4)
    assert np.all(identity_matrix == np.eye(4))


def test_manipulate_matrices():
    zeros_matrix, ones_matrix, identity_matrix = create_matrices()
    zeros_matrix_modif, ones_matrix_modif, identity_matrix_modif = manipulate_matrices(
        zeros_matrix, ones_matrix, identity_matrix
    )

    # Prueba para la matriz de ceros modificada
    expected_zeros_modif = np.zeros((3, 3))
    expected_zeros_modif[1, 1] = 5
    assert np.array_equal(zeros_matrix_modif, expected_zeros_modif)

    # Prueba para la matriz de unos modificada
    expected_ones_modif = np.ones((2, 4))
    expected_ones_modif[:, 2] = 3
    assert np.array_equal(ones_matrix_modif, expected_ones_modif)

    # Prueba para la matriz identidad modificada
    expected_identity_modif = np.eye(4)
    expected_identity_modif[np.arange(4), np.arange(3, -1, -1)] = 2
    assert np.array_equal(identity_matrix_modif, expected_identity_modif)
