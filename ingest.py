import requests
import os

# Novo URL do CSV (dados de voos mensais)
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
local_csv_path = "data/raw.csv"

def download_data():
    print("🔽 A fazer download do ficheiro CSV...")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(local_csv_path, "wb") as f:
        f.write(response.content)
    print(f"✔️  Download concluído: {local_csv_path}")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    download_data()
