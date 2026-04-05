def secure_archive(file_name: str, mode: str, content: str) -> tuple:
    try:
        if mode == "r" or mode == "w":
            action = mode
        else:
            return (False, "Invalid mode: nice try Didi :)>")
        with open(file_name, action) as file:
            if action == "r":
                content = file.read()
                return (True, content)
            elif action == "w":
                file.write(content)
                return (True, "Content successfully written to file")
    except FileNotFoundError as e:
        return (False, f"{e}")
    except PermissionError as e:
        return (False, f"{e}")
    except Exception as e:
        return (False, f"{e}")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    my_tupe = secure_archive("/not/existing/file", "r", "")
    print(my_tupe, "\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    my_tupe = secure_archive("master.passwdd", "r", "")
    print(my_tupe, "\n")
    print("Using 'secure_archive' to read from a regular file:")
    my_tupe = secure_archive("youness", "r", "")
    print(my_tupe, "\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    my_tupe = secure_archive("hamid", "w", my_tupe[1])
    print(my_tupe)


if __name__ == "__main__":
    main()
