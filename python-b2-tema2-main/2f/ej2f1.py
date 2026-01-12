"""
Enunciado:
Desarrolla un conjunto de funciones que permitan cargar, guardar y visualizar el conjunto de datos de vinos mediante
Pandas, Matplotlib, Seaborn y Pickle.

Funciones a desarrollar:
- create_histograms(df: DataFrame, features: List[str]) -> matplotlib.figure.Figure:
    Descripción:
    Genera histogramas para un conjunto de datos de vinos, diferenciando las muestras según su clase de vino.
    Parámetros:
        - df (pd.DataFrame): DataFrame que contiene los datos del conjunto de vinos.
        - features (List[str]): Lista de nombres de las características para las cuales se generarán los histogramas.

- save_img_pickle(fig: Figure, filename: str) -> None:
    Descripción:
    Guarda una figura de Matplotlib en un archivo utilizando Pickle, lo que permite su recuperación y visualización
    posterior sin necesidad de regenerar el gráfico.
    Parámetros:
        - fig (matplotlib.figure.Figure): Figura que se desea guardar.
        - filename (str): Ruta del archivo donde se guardará la figura.

- load_and_display_figure(filename: str) -> matplotlib.figure.Figure:
    Descripción:
    Carga y muestra una figura guardada previamente desde un archivo.
    Parámetros:
        - filename (str): Ruta del archivo donde se encuentra guardada la figura.

Ejemplo:
    df_wine = pd.DataFrame(data=wine.data, columns=wine.feature_names)
    df_wine['target'] = pd.Categorical.from_codes(wine.target, wine.target_names)

    fig_histograms = create_histograms(df_wine, df_wine.columns[:6])
    save_figure(fig_histograms, 'data/histograms_wine.pickle')

Salida esperada:
- Visualización de histogramas para las primeras seis características del conjunto de datos de vinos, con
diferenciación por clase de vino.
- Guardar en un archivo la figura que contiene el histograma, permitiendo su posterior recuperación y visualización
sin regenerar los gráficos.
"""

from sklearn.datasets import load_wine
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from typing import List, Union
from matplotlib.figure import Figure
from pandas.core.frame import DataFrame
from pathlib import Path


def create_histograms(df: DataFrame, features: List[str]) -> Figure:

    n_features = len(features)
    fig, axes = plt.subplots(n_features, 1, figsize=(8, 4 * n_features))

    if n_features == 1:
        axes = [axes]

    for ax, feature in zip(axes, features):
        sns.histplot(
            data=df,
            x=feature,
            hue="target",
            multiple="stack",
            ax=ax
        )
        ax.set_title(f"Histogram of {feature}")

    plt.tight_layout()
    return fig


def save_img_pickle(fig: Figure, filename: str) -> None:

    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "wb") as f:
        pickle.dump(fig, f)

def load_and_display_figure(filename: str) -> Figure:
    with open(filename, "rb") as f:
        fig = pickle.load(f)

    return fig

# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
     wine = load_wine()
     df_wine = pd.DataFrame(data=wine.data, columns=wine.feature_names)
     df_wine["target"] = pd.Categorical.from_codes(wine.target, wine.target_names)

     fig_histograms = create_histograms(df_wine, df_wine.columns[:6])
     is_saved = save_img_pickle(fig_histograms, "data/histograms_wine.pickle")
     print("Figure saved:", is_saved)
     fig_loaded = load_and_display_figure("data/histograms_wine.pickle")
     plt.show()
