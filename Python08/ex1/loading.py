import sys
import importlib as imp


if __name__ == "__main__":
    missing_dependencies = False
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    try:
        pd = imp.import_module("pandas")
        print(f"[OK] {pd.__name__} ({pd.__version__}) "
              "- Data manipulation ready")
    except ImportError as e:
        print(f"[MISSING PACKAGE] {e.name} is not installed.")
        missing_dependencies = True

    try:
        rq = imp.import_module("requests")
        print(f"[OK] {rq.__name__} ({rq.__version__}) "
              "- Network access ready")
    except ImportError as e:
        print(f"[MISSING PACKAGE] {e.name} is not installed.")

    try:
        mplt = imp.import_module("matplotlib")
        print(f"[OK] {mplt.__name__} ({mplt.__version__}) "
              "- Visualization ready")
        import matplotlib.pyplot as plt
    except ImportError as e:
        print(f"[MISSING PACKAGE] {e.name} is not installed.")
        missing_dependencies = True

    try:
        np = imp.import_module("numpy")
    except ImportError as e:
        print(f"[MISSING PACKAGE] {e.name} is not installed.")
        missing_dependencies = True

    if missing_dependencies:
        print("Please install required packages:")
        print("pip install -r requirements.txt")
        print("OR")
        print("poetry install")
        print("poetry run python loading.py")
        sys.exit(1)

    print("\nAnalyzing Matrix data...")
    x = np.arange(1000)
    y = np.random.normal(0, 1, size=1000)

    df = pd.DataFrame({
        "tick": x,
        "signal": y
    })

    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")
    plt.plot(df["tick"], df["signal"])
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
