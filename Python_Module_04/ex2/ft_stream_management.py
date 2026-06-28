import sys


def main() -> None:
    if len(sys.argv) == 2:
        sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
        argument = sys.argv[1].strip()
        sys.stdout.write(f"Accessing file '{argument}'\n")
        try:
            file = open(argument, "r")
            content = file.read()
            sys.stdout.write("---\n")
            sys.stdout.write(content)
            sys.stdout.write("---\n")
        except FileNotFoundError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
            return
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
            return
        except Exception as e:
            sys.stderr.write(
                f"[STDERR] Error opening file "
                f"'{argument}': {e}\n"
                )
            return
        finally:
            file.close()
            print(f"File '{argument}' closed.\n")
        try:
            sys.stdout.write("Transform data:\n")
            sys.stdout.write("---\n")
            search = content.replace("\n", "#\n")
            sys.stdout.write(search)
            sys.stdout.write("---\n")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            new_file = sys.stdin.readline()
            new_file = new_file.strip()
            if new_file:
                sys.stdout.write(f"Saving data to '{new_file}'")
                file = open(new_file, "w")
                file.write(search)
            else:
                sys.stdout.write("Not saving data.\n")
        except FileNotFoundError as e:
            sys.stderr.write(
                f"[STDERR] Error opening file "
                f"'{argument}': {e}\n"
                )
            return
        except Exception as e:
            sys.stderr.write(f"Error {e}\n")
            sys.stdout.write("Not saving data.\n")
        finally:
            sys.stdout.write(f"\nData saved in file '{new_file}'\n")
            file.close()
    else:
        sys.stdout.write(f"Usage: {sys.argv[0]} <file>\n")


if __name__ == "__main__":
    main()
