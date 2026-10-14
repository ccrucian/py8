import importlib
import sys
from importlib.metadata import PackageNotFoundError, version


def analyze_matrix_data() -> None:
    """Generate Matrix data, analyze it, and save a visualization."""
    import matplotlib
    import numpy as np
    import pandas as pd

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    rng = np.random.default_rng(42)
    data = rng.integers(0, 100, size=1000)

    df = pd.DataFrame({"Data": data})
    print("Processing", len(df), "data points...")
    print(f"Mean: {df['Data'].mean():.2f}")
    print(f"Standard deviation: {np.std(data):.2f}")

    print("Generating visualization...")
    fig, ax = plt.subplots()
    try:
        ax.hist(data, bins=10, edgecolor="red")
        ax.set_title("Matrix Data Distribution")
        ax.set_xlabel("Simulated value")
        ax.set_ylabel("Count")
        fig.savefig("matrix_analysis.png")
    finally:
        plt.close(fig)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def check_dependency(name: str) -> bool:
    """Check that a package can actually be imported."""
    try:
        importlib.import_module(name)
        return True
    except ImportError:
        return False


def package_version(name: str) -> str:
    """Read the installed version from package metadata."""
    try:
        return version(name)
    except PackageNotFoundError:
        return "Unknown version"


def compare_dependency_management() -> bool:
    """Show installed versions and compare pip and Poetry workflows."""
    print("\nChecking dependencies:")
    print("Current Python:", sys.executable)
    dependencies = ["numpy", "pandas", "matplotlib"]
    installed = True

    for name in dependencies:
        if check_dependency(name):
            print(f"[OK] {name} ({package_version(name)})")
        else:
            print(f"[MISSING] {name}")
            installed = False

    print("\nDependency management comparison:")
    print("pip installs packages listed in requirements.txt.")
    print("Create and activate a virtual environment before installing.")
    print("  python3 -m pip install -r requirements.txt")
    print("  python3 loading.py")

    print("\nPoetry manages dependencies declared in pyproject.toml.")
    print("It can create a virtual environment and records resolved versions")
    print("in poetry.lock for reproducible installations.")
    print("  poetry install")
    print("  poetry run python loading.py")
    print("\nThe versions above belong to the current Python environment.")
    return installed


def main() -> None:
    """Check dependencies and report analysis errors without a traceback."""
    print("LOADING STATUS: Loading programs...")

    if not compare_dependency_management():
        print("Cannot analyze data: missing dependencies.")
        print("Install them using one of the workflows shown above.")
        return

    try:
        analyze_matrix_data()
    except (ImportError, OSError, ValueError, RuntimeError) as e:
        print(f"Analysis failed: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
