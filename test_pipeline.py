import os
import pandas as pd
from sqlalchemy import create_engine

# 1. Test if raw data file exists
def test_raw_file_exists():
    assert os.path.exists("data/raw.csv"), "Raw CSV file not found."

# 2. Test if cleaned CSV has expected structure
def test_cleaned_file_structure():
    df = pd.read_csv("data/cleaned.csv")
    expected_columns = {"Month", "Year", "Passengers"}
    assert set(df.columns) == expected_columns, f"Unexpected columns: {df.columns.tolist()}"

# 3. Test if cleaned file has expected number of rows (should be 12 months * 3 years)
def test_cleaned_row_count():
    df = pd.read_csv("data/cleaned.csv")
    assert len(df) == 36, f"Unexpected number of rows: {len(df)}"

# 4. Test if SQLite DB exists and contains data
def test_sqlite_data_loaded():
    engine = create_engine("sqlite:///data/airtravel.db")
    df = pd.read_sql("SELECT COUNT(*) as count FROM flights", engine)
    assert df.loc[0, "count"] == 36, "Expected 36 rows in the database table."

# 5. Test if no missing values exist in cleaned data
def test_no_nulls_in_cleaned_data():
    df = pd.read_csv("data/cleaned.csv")
    assert df.isnull().sum().sum() == 0, "There are missing values in the cleaned dataset."
