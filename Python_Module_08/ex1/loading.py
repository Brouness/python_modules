import sys
try:
    import importlib
    import matplotlib.pyplot as plt  # type: ignore
    import numpy  # type: ignore
    import pandas  # type: ignore
except ModuleNotFoundError:
    print("*WARNING MISSING DEPENDENCIES*")
    print("*INSTRUCTIONS TO FOLLOW*")
    print("Run:")
    print("pip install -r requirement.txt")
    print("poetry install")
    print("NOTICE:!!! if poetry didn't work run the following command")
    print("pip install poetry")
    sys.exit()


def generate_matrix_data() -> pandas.DataFrame:
    print("Processing 1000 data points...")
    df = pandas.DataFrame(
        {
            "signal": numpy.random.randn(1000),
            "noise": numpy.random.randn(1000)
            }
            )
    return df


def check_dependencies(my_list: dict[str, str]) -> None:
    print("Checking dependencies:")
    for package, description in my_list.items():
        if importlib.util.find_spec(package):  # type: ignore
            print(f"[OK] {package} {description}")
        else:
            print(f"[MISSING] {package} - "
                  f"Please install: pip install {package}")


def generate_visualization(df: pandas.DataFrame) -> None:
    print("Generating visualization...")
    fig, ax = plt.subplots()
    ax.plot(df["signal"], label="signal")
    ax.plot(df["noise"], label="noise")
    ax.set_title("Matrix Data Analysis")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.legend()
    plt.savefig("matrix_analysis.png")


def main() -> None:
    packages: dict[str, str] = {
        "pandas": "(2.1.0) - Data manipulation ready",
        "numpy": "(1.25.0) - Numerical computation ready",
        "requests": "(2.31.0) - Network access ready",
        "matplotlib": "(3.7.2) - Visualization ready"
    }
    print("\nLOADING STATUS: Loading programs...\n")
    check_dependencies(packages)
    print("\nAnalyzing Matrix data...")
    df: pandas.DataFrame = generate_matrix_data()
    generate_visualization(df)
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
