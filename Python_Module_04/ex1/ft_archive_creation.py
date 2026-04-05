import sys


def main() -> None:
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1], "r")
            content = file.read()
            print("---\n")
            print(content)
            print("---")
        except FileNotFoundError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
            return
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
            return
        except BaseException as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
            return
        finally:
            file.close()
            print(f"File '{sys.argv[1]}' closed.\n")
        try:
            print("Transform data:")
            print("---\n")
            search = content.replace("\n", "#\n")
            print(search)
            print("---")
            new_file = input("Enter new file name (or empty): ")
            if new_file:
                print(f"saving data to '{new_file}'")
                file = open(new_file, "w")
                file.write(search)
                file.close()
                print(f"Data saved in file {new_file}\n")
            else:
                print("Not saving data.")
        except KeyboardInterrupt as e:
            print(f"Nice try Didi :)> {e}")
        except FileNotFoundError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
            return
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
            return
        except BaseException as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
            return
        except Exception as e:
            print(f"Error: {e}")
            print("Not saving data.")
        finally:
            file.close()
    else:
        print(f"Usage: {sys.argv[0]} <file>\n")


if __name__ == "__main__":
    main()
