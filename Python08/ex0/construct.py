import sys
import os
import site


if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected\n")
        print("WARNING: You are in the global Python environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate    # On Windows\n")
        print("Then run this program again.")

    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment:", os.path.basename(sys.prefix))
        print("Environment Path:", sys.prefix, "\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("\nPackage installation path:")
        try:
            for path in site.getsitepackages():
                print(path)
        except Exception:
            print("Path not found")
