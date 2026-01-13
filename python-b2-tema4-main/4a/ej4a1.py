"""
Enunciado:
Desarrolla un paquete de Python llamado `datalib` destinado a cargar y analizar conjuntos de datos almacenados en
archivos CSV.

Estructura y Componentes del Paquete:
- `datalib/loader.py`:
    - `load_csv(filepath)`: Función para cargar datos desde un archivo CSV, retornando una lista de diccionarios, donde
    cada diccionario representa una fila del archivo CSV.

- `datalib/stats.py`:
    - `mean(data, key)`: Función para calcular la media de los valores numéricos de una clave específica en una lista
    de diccionarios.
    - `median(data, key)`: Función para calcular la mediana de los valores numéricos de una clave específica en una
    lista de diccionarios.

- `datalib/__init__.py`:
    - Importa y expone las funciones `load_csv` del módulo `loader` y las funciones `mean` y `median` del módulo 
    `stats`.

Instrucciones de Implementación:
1. Crea la estructura de directorios propuesta para el paquete `datalib`.
2. Implementa las funciones especificadas en los módulos `loader.py` y `stats.py` siguiendo las indicaciones.
3. Asegúrate de que los módulos `__init__.py` importen y expongan correctamente las funciones.
4. Utiliza buenas prácticas de programación en Python, incluyendo documentación adecuada de las funciones y manejo de
excepciones si es necesario.

Ejemplo de Uso:
Imagina que quieres cargar un conjunto de datos desde un archivo CSV y luego calcular la media y la mediana de una
columna numérica específica. Con el paquete `datalib`, podrás hacerlo fácilmente importando las funciones necesarias y
aplicándolas a tu conjunto de datos.

Salida esperada:
- Carga exitosa de datos desde un archivo CSV en una estructura de datos manejable en Python.
- Cálculo correcto de la media y la mediana de columnas específicas en el conjunto de datos.
- Estructura de paquete coherente que facilita la importación y utilización de sus componentes para tareas de carga y
análisis de datos.
"""

from datalib import load_csv, mean, median
from pathlib import Path


#Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
     filepath = Path(__file__).parent / "data/grades.csv"

     data = load_csv(filepath)

     key = "Hindi"
     mean_value = mean(data, key)
     median_value = median(data, key)

     print(f"Mean de '{key}': {mean_value}")
     print(f"Median de '{key}': {median_value}")
