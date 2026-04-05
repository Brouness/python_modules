import sys


def main() -> None:
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1], "r")
            content = file.read()
            print("---")
            print(content)
            print("---")
        except FileNotFoundError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
        except BaseException as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
        finally:
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
    else:
        print(f"Usage: {sys.argv[0]} <file>\n")


if __name__ == "__main__":
    main()
