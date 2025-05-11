import pandas as pd
from sqlalchemy import create_engine

# Paths
input_path = "data/cleaned.csv"
db_path = "data/airtravel.db"

def save_to_sqlite():
    # Load the cleaned CSV
    df = pd.read_csv(input_path)

    # Convert column types
    df["Passengers"] = pd.to_numeric(df["Passengers"], errors="coerce")

    # Create SQLite engine
    engine = create_engine(f"sqlite:///{db_path}")

    # Save to table 'flights'
    df.to_sql("flights", engine, if_exists="replace", index=False)
    print(f"✅ Data saved to SQLite database at: {db_path}")

    # Example query (optional)
    result = pd.read_sql("SELECT Year, SUM(Passengers) as total FROM flights GROUP BY Year", engine)
    print("\n📊 Total passengers by year:")
    print(result)

if __name__ == "__main__":
    save_to_sqlite()
