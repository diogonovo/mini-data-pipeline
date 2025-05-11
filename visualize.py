import pandas as pd
import matplotlib.pyplot as plt

input_path = "data/cleaned.csv"

def plot_data():
    print("📈 Loading data...")
    df = pd.read_csv(input_path)
    print("\nUnique months:", df["Month"].unique())


    # Print preview of the loaded data
    print("\n--- Raw Data Preview ---")
    print(df.head())
    print(df.dtypes)

    # Ensure Passengers is numeric
    df["Passengers"] = pd.to_numeric(df["Passengers"], errors="coerce")

    # Drop rows with missing values
    df = df.dropna(subset=["Passengers", "Year", "Month"])

    print("\n--- Cleaned Data Preview ---")
    print(df.head())
    print(df.dtypes)

    # Pivot the data
    try:
        pivot_df = df.pivot_table(index="Month", columns="Year", values="Passengers", aggfunc="sum")
        print("\n--- Pivot Table ---")
        print(pivot_df)
    except Exception as e:
        print("❌ Pivot error:", e)
        return

    print("🗂️ Preparing plot...")
    pivot_df.plot(kind="bar", figsize=(10, 6))
    plt.title("Monthly Air Passengers (1958–1960)")
    plt.xlabel("Month")
    plt.ylabel("Number of Passengers")
    plt.legend(title="Year")
    plt.tight_layout()
    plt.savefig("data/plot.png")
    print("✅ Plot saved to data/plot.png")

if __name__ == "__main__":
    plot_data()
