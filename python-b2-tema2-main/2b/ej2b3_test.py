import pandas as pd
from pathlib import Path
from ej2b3 import read_sqlite_table, execute_sqlite_query

current_dir = Path(__file__).parent
TEST_DB_PATH = current_dir / "data/ej2b3/ramen-ratings.db"
TEST_TABLE_NAME = "ramen_ratings"


def test_read_sqlite_table():
    df = read_sqlite_table(TEST_DB_PATH, TEST_TABLE_NAME)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_execute_sqlite_query():
    query = "SELECT * FROM ramen_ratings WHERE Stars >= 4"
    df = execute_sqlite_query(TEST_DB_PATH, query)
    df["Stars"] = pd.to_numeric(df["Stars"], errors="coerce")
    df = df.dropna(subset=["Stars"])

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert all(df["Stars"] >= 4)
