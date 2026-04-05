import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    if len(sys.argv) == 1:
        print("Nice try DIDI :)")
        return
    else:
        full_dict = {}
        for arg in sys.argv[1:]:
            if ":" in arg:
                name, value = arg.split(":")
                if name in full_dict:
                    print(f"Redundant item '{name}' - discarding")
                else:
                    try:
                        full_dict[name] = int(value)
                    except ValueError as e:
                        print(f"Quantity error for '{name}': {e}")
            else:
                print(f"Error - invalid parameter '{arg}'")
        print(f"Got inventory: {full_dict}")
        print(f"Item list: {list(full_dict.keys())}")
        number_of_keys = len(full_dict.keys())
        total_quantity = sum(full_dict.values())
        print(f"Total quantity of the {number_of_keys} "
              f"items: {total_quantity}")
        for key in full_dict:
            break
        max_item = key
        min_item = key
        for item in full_dict:
            if full_dict[item] > full_dict[max_item]:
                max_item = item
            if full_dict[item] < full_dict[min_item]:
                min_item = item
            percentage = full_dict[item] / total_quantity * 100
            print(f"Item {item} represents {round(percentage, 1)}%")
        print(f"Item most abundan: {max_item} with quantity "
              f"{full_dict[max_item]}")
        print(f"Item most abundan: {min_item} with quantity "
              f"{full_dict[min_item]}")
        full_dict.update({"magic_item": 1})
        print(f"Updated inventory: {full_dict}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Caught an Error: {e}")
        print("Program didn't crash!!")
