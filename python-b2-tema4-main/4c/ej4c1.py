"""
Enunciado:
Desarrolla un test para la función implementada calculate_rectangle_area, la función recibe dos parámetros ancho y
alto, y devuelve el área del rectángulo, calculada como ancho * alto. utilizando el enfoque de Desarrollo Guiado
por Pruebas (TDD).

Se debe realizar los test en el archivo ej4c1_test.py considerando los distintos casos de prueba especificados en el
test.
"""

def calculate_rectangle_area(width: int, height: int) -> int:
    if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
        raise TypeError("Width and height must be numbers.")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    
    area = width * height
    return area

# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
     print(calculate_rectangle_area(5, 10))
