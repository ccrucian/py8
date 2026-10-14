
import os
import site
import sys


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def show_environment_info() -> None:
    print("Current Python:", sys.executable)
    print("Environment path:", sys.prefix)
    print("Base Python path:", sys.base_prefix)

    print("\nPackage installation paths:")
    for path in site.getsitepackages():
        print(path)


def main() -> None:
    if is_virtual_environment():
        print("MATRIX STATUS: Welcome to the construct\n")

        show_environment_info()

        env_name = os.path.basename(sys.prefix)
        print("\nVirtual Environment:", env_name)
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

    else:
        print("MATRIX STATUS: You're still plugged in\n")

        show_environment_info()

        print("\nVirtual Environment: None detected")
        print("WARNING: You're in the global environment!")

        print("\nTo enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate  # Linux/macOS")
        print(r"matrix_env\Scripts\activate.bat  # Windows CMD")
        print(r".\matrix_env\Scripts\Activate.ps1  # Windows PowerShell")

        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
