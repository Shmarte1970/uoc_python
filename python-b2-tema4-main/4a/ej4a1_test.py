import pytest
import os


@pytest.fixture
def sample_csv(tmpdir):
    csv_content = "name,age\nJohn,25\nAlice,30\nBob,35"
    csv_file = tmpdir.join("test.csv")
    csv_file.write(csv_content)
    return csv_file


def test_import_loader():
    try:
        from datalib import loader

        assert True, "The loader module was imported successfully."
    except ImportError as e:
        pytest.fail(f"Failed to import the loader module: {e}")


def test_import_stats():
    try:
        from datalib import stats

        assert True, "The stats module was imported successfully."
    except ImportError as e:
        pytest.fail(f"Failed to import the stats module: {e}")


def test_load_csv_exists():
    from datalib import loader

    assert hasattr(
        loader, "load_csv"
    ), "The load_csv function was not found in the loader module."


def test_stats_functions_exists():
    from datalib import stats

    assert hasattr(
        stats, "mean"
    ), "The mean function was not found in the stats module."
    assert hasattr(
        stats, "median"
    ), "The median function was not found in the stats module."


def test_load_csv(sample_csv):
    from datalib.loader import load_csv
    
    data = load_csv(sample_csv)
    assert len(data) == 3
    assert data[0]["name"] == "John"
    assert data[1]["age"] == "30"


def test_mean():
    from datalib.stats import mean
    
    data = [{"value": 10}, {"value": 20}, {"value": 30}]
    assert mean(data, "value") == 20


def test_median_odd():
    from datalib.stats import median
    
    data = [{"value": 10}, {"value": 20}, {"value": 30}, {"value": 40}, {"value": 50}]
    assert median(data, "value") == 30


def test_median_even():
    from datalib.stats import median
    
    data = [{"value": 10}, {"value": 20}, {"value": 30}, {"value": 40}]
    assert median(data, "value") == 25.0
