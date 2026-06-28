import sys
import os
import site


def is_in_venv() -> bool:
    if sys.prefix == sys.base_prefix:
        return False
    else:
        return True


def main() -> None:
    permission: bool = is_in_venv()
    status: str = (
        " Welcome to the construct" if permission
        else " You're still plugged in"
            )
    venv: str = "VIRTUAL_ENV"
    print(F"MATRIX STATUS:{status}\n")
    print(f"Current Python: {sys.executable}")
    if permission:
        print(f"Virtual Environment: {os.environ.get(venv)}")
        print(f"Environment Path: {os.environ.get(venv)}")
        print("\nSUCCESS: You're in an isolated environment!")
        print(
            "Safe to install packages without affecting\nthe global system."
                    )
        print(f"\nPackage installation path:\n{site.getsitepackages()[0]}")
    else:
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machine can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
