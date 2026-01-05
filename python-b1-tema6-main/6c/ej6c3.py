"""
Enunciado:
Implementa un código capaz de leer archivos 'parquet' para luego calcular
la columna 'amount' del DataFrame resultante. En este caso, el archivo
parquet tiene las ventas de una tienda de un mes.

Para ello se crean dos funciones.

La primera llamada 'read_parquet_file(path)' que recibe como parámetro
'path' y retorna el DataFrame que se encuentra en la ruta en formato
parquet.

La segunda función llamada 'calculate_amount_quantity(dataframe)' que
recibe como parámetro un DataFrame y calcula la columna 'amount' como el
producto de la columna 'price' y la columna 'units_sold'. La función retorna
el DataFrame con la nueva columna calculada.

Se debe leer el archivo parquet que se encuentra en la ruta: 
"files/sales_products_2020_08.parquet".


Función 'read_parquet_file(path)'
    Parámetros:
        path (string): Representa la ruta al archivo parquet.
    Retorna:
        pd.DataFrame: Contenido del archivo parquet.

Función 'calculate_amount_quantity(dataframe)'
    Parámetros:
        dataframe (pd.DataFrame): Representa el DataFrame a procesar.
    Retorna:
        pd.DataFrame: DataFrame con la nueva columna 'amount' calculada.

Ejemplo:
    Entrada:
        df = read_parquet_file(path)
        df_result = calculate_amount_quantity(df)
        print(df_result.columns)
    Salida:
        Index(['title', 'price', 'retail_price', 'units_sold', 'rating',
        'rating_count', 'product_id', 'crawl_month', 'amount'],
        dtype='object')


Enunciat:
Implementa un codi capaç de llegir arxius 'parquet' per després calcular
la columna 'amount' del DataFrame resultant. En aquest cas, el fitxer
parquet té les vendes d´una botiga d´un mes.

Per això es creen dues funcions.

La primera anomenada 'read_parquet_file(path)' que rep com a paràmetre
'path' i retorna el DataFrame que es troba a la ruta en format
parquet.

La segona funció anomenada 'calculate_amount_quantity(dataframe)' que
rep com a paràmetre un DataFrame i calcula la columna 'amount' com el
producte de la columna 'price' i la columna 'units_sold'. La funció retorna
el DataFrame amb la nova columna calculada.

Cal llegir el fitxer parquet que es troba a la ruta:
"files/sales_products_2020_08.parquet".


Funció 'read_parquet_file(path)'
     Paràmetres:
         path (string): Representa la ruta al fitxer parquet.
     Retorna:
         pd.DataFrame: Contingut del fitxer parquet.

Funció 'calculate_amount_quantity(dataframe)'
     Paràmetres:
         dataframe (pd.DataFrame): Representa el DataFrame a processar.
     Retorna:
         pd.DataFrame: DataFrame amb la nova columna 'amount' calculada.

Exemple:
     Entrada:
         df = read_parquet_file(path)
         df_result = calculate_amount_quantity(df)
         print(df_result.columns)
     Sortida:
         Index(['title', 'price', 'retail_price', 'units_sold', 'rating',
         'rating_count', 'product_id', 'crawl_month', 'amount'],
         dtype='object')

"""


import pandas as pd

def read_parquet_file(path: str) -> pd.DataFrame:
    """Lee un archivo parquet y retorna un DataFrame."""
    return pd.read_parquet(path)


def calculate_amount_quanity(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Calcula la columna 'amount' como price * units_sold."""
    dataframe["amount"] = dataframe["price"] * dataframe["units_sold"]
    return dataframe


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# df_sales = read_parquet_file("files/sales_products_2020_08.parquet")
# print(df_sales.columns)
#
# df_sales = calculate_amount_quanity(df_sales)
# print(df_sales.columns)
# print(df_sales[["price", "units_sold", "amount"]].head())
