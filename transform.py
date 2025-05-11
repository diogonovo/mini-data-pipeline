import pandas as pd

# File paths
input_path = "data/raw.csv"
output_path = "data/cleaned.csv"

def transform():
    print("🔄 Transforming data...")

    # Read raw CSV (with possible spaces in headers and values)
    df = pd.read_csv(input_path)

    # Strip quotes and spaces from column names
    df.columns = df.columns.str.strip().str.replace('"', '')

    # Clean month values
    df["Month"] = df["Month"].astype(str).str.strip().str.replace('"', '')

    # Melt the DataFrame from wide to long
    df_long = df.melt(id_vars="Month", var_name="Year", value_name="Passengers")

    # Convert to correct types
    df_long["Passengers"] = pd.to_numeric(df_long["Passengers"], errors="coerce")
    df_long["Year"] = df_long["Year"].astype(str)

    # Month ordering
    df_long["Month"] = pd.Categorical(
        df_long["Month"],
        categories=["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
                    "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"],
        ordered=True
    )

    df_long = df_long.sort_values(by=["Year", "Month"])

    # Save cleaned version
    df_long.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    transform()
