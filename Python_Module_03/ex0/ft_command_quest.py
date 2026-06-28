import sys

if __name__ == "__main__":
    try:
        print("=== Command Quest ===")
        print(f"Program name: {sys.argv[0]}")
        if len(sys.argv) == 1:
            print(f"No arguments provided\n"
                  f"Total arguments: {len(sys.argv)}\n")
        else:
            print(f"Arguments received: {len(sys.argv) - 1}")
            idx = 1
            for i in range(len(sys.argv) - 1):
                print(f"Argument {idx}: {sys.argv[idx]}")
                idx += 1
            print(f"Total arguments: {len(sys.argv)}\n")
    except Exception as e:
        print(f"Caught Unknown Error: {e}")
