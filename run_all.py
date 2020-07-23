import os
import subprocess


EXCEPTIONS = ("guess.py", "parallel.py", "run_all.py")


def run_python_files():
    for file in os.listdir("."):
        if file.endswith(".py") and file not in EXCEPTIONS:
            print(f"Running {file}")
            subprocess.run(["python", file])


if __name__ == "__main__":
    run_python_files()
