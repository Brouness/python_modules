from collections.abc import Callable


def mage_counter() -> Callable:
    count: int = 0

    def inner() -> int:
        nonlocal count
        count += 1
        return count
    return inner


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def inner(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return inner


def enchantment_factory(enchantment_type: str) -> Callable:
    def inner(item: str) -> str:
        return f"{enchantment_type} {item}"
    return inner


def memory_vault() -> dict[str, Callable]:
    storage: dict = {}

    def store(key: str, Value: str) -> None:
        storage[key] = Value

    def recall(key: str) -> str:
        return storage.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print("\nTesting spell accumulator...")
    base_spell = spell_accumulator(100)
    print(f"Base 100, add 20: {base_spell(20)}")
    print(f"Base 100, add 30: {base_spell(30)}")
    print("\nTesting enchantment factory...")
    enchantment_a = enchantment_factory("Flaming")
    enchantment_b = enchantment_factory("Frozen")
    print(enchantment_a("Sword"))
    print(enchantment_b("Shield"))
    print("\nTesting memory vault...")
    my_dict: dict[str, Callable] = memory_vault()
    my_dict['store']("secret", 42)
    print("Store 'secret' = 42")
    recall = my_dict['recall']("secret")
    print(f"Recall 'secret' : {recall}")
    recall = my_dict['recall']("unknown")
    print(f"Recall 'unknown': {recall}")


if __name__ == "__main__":
    main()
