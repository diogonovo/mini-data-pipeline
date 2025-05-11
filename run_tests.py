import subprocess

def run_pytest():
    print("🧪 Running tests with pytest...")
    result = subprocess.run(["pytest"], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    run_pytest()
