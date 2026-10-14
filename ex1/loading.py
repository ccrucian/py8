import importlib
from importlib.metadata import (
        version, PackageNotFoundError
        )


def analyze_matrix_data() -> None:

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    rng = np.random.default_rng(42)
    data = rng.integers(0, 100, size=1000)

    df = pd.DataFrame({"Data": data})
    print("Processing", len(df), "data point...")
    print("Mean:", df["Data"].mean())

    plt.hist(data, bins=10, edgecolor="red")
    plt.title("Matrix Data Distribution")
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def check_dependency(name: str) -> bool:
    try:
        importlib.import_module(name)
        return True
    except ImportError:
        return False


def package_version(name: str) -> str:
    try:
        return version(name)
    except PackageNotFoundError:
        return "Unknown version"


def main() -> None:
    print("LOADING STATUS: Loading programs...")

    dependencies = ["numpy", "pandas", "matplotlib"]
    installed = True

    for name in dependencies:
        if check_dependency(name):
            print(
                f"[OK] {name} ({package_version(name)})"
                )
        else:
            print(f"[MISSING] {name}")
            installed = False

    if installed:
        analyze_matrix_data()
    else:
        print("Cannot analyze data: missing dependencies.")
        print("\nInstall dependencies with pip:")
        print("pip install -r requirements.txt")

        print("\nOr install with Poetry:")
        print("poetry install")


if __name__ == "__main__":
    main()
