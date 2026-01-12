import numpy as np
from ej2a4 import (
    compare_monthly_sales,
)


def test_enhanced_compare_monthly_sales_creates_figure_and_axes():
    sales_2020 = np.random.randint(100, 500, 12)
    sales_2021 = np.random.randint(100, 500, 12)
    sales_2022 = np.random.randint(100, 500, 12)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    fig, ax1, ax2 = compare_monthly_sales(sales_2020, sales_2021, sales_2022, months)
    assert fig is not None, "The function should create a Matplotlib figure"
    assert ax1 is not None, "The function should create the first Matplotlib axis"
    assert ax2 is not None, "The function should create the second Matplotlib axis"


# Test para verificar las características específicas de ax1 (Gráfico de barras y líneas)
def test_ax1_features():
    sales_2020 = np.random.randint(100, 500, 12)
    sales_2021 = np.random.randint(100, 500, 12)
    sales_2022 = np.random.randint(100, 500, 12)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    _, ax1, _ = compare_monthly_sales(sales_2020, sales_2021, sales_2022, months)
    assert (
        ax1.title.get_text() == "Monthly Sales Comparison: 2020 vs 2021"
    ), "The title of ax1 should be correct"
    assert (
        len(ax1.patches) == 24
    ), "There should be 24 bars in the bar chart (12 for each year)"


# Test para verificar las características específicas de ax2 (Gráfico de pastel)
def test_ax2_features():
    sales_2020 = np.random.randint(100, 500, 12)
    sales_2021 = np.random.randint(100, 500, 12)
    sales_2022 = np.random.randint(100, 500, 12)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    _, _, ax2 = compare_monthly_sales(sales_2020, sales_2021, sales_2022, months)
    assert (
        ax2.title.get_text() == "2022 Monthly Sales Distribution"
    ), "The title of ax2 should be correct"
    assert (
        len(ax2.patches) == 12
    ), "There should be 12 segments in the pie chart (one for each month)"


# Test adicional para verificar si la longitud de los datos y las etiquetas coinciden
def test_data_label_length_match():
    sales_2020 = np.random.randint(100, 500, 12)
    sales_2021 = np.random.randint(100, 500, 12)
    sales_2022 = np.random.randint(100, 500, 12)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    assert len(sales_2020) == len(
        months
    ), "Length of sales data and month labels must match for the first year"
    assert len(sales_2021) == len(
        months
    ), "Length of sales data and month labels must match for the second year"
    assert len(sales_2022) == len(
        months
    ), "Length of sales data and month labels must match for the third year"
