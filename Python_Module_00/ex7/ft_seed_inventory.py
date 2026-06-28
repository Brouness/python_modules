def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    s = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{s} seeds: {quantity} {unit} available")
    elif (unit == "grams"):
        print(f"{s} seeds: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{s} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
