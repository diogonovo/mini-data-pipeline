from prefect import flow, task
import subprocess

@task
def ingest():
    subprocess.run(["python", "ingest.py"], check=True)

@task
def transform():
    subprocess.run(["python", "transform.py"], check=True)

@task
def save_to_db():
    subprocess.run(["python", "save_to_db.py"], check=True)
    
@task
def run_tests():
    subprocess.run(["python", "run_tests.py"], check=True)

@flow(name="Air Travel Pipeline Flow")
def run_pipeline():
    ingest()
    transform()
    save_to_db()
    run_tests()


if __name__ == "__main__":
    run_pipeline()
