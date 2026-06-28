from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
import operator as op


def spell_reducer(spells: list[int], opperation: str) -> int:
    if not spells:
        return 0
    my_dic: dict[str, Callable] = {
        'add': op.add,
        'multiply': op.mul,
        'max': lambda a, b: max(a, b),
        'min': lambda a, b: min(a, b)
    }
    for key, value in my_dic.items():
        if opperation == key:
            return reduce(value, spells)
    raise ValueError(f"ERROR invalid opperayion: {opperation}" +
                     " uses: 'add' or 'mul', 'min', 'max'")


def partial_enchanter(base_enchantement: Callable) -> dict:
    partial_fire = partial(base_enchantement, 50, "Fire")
    partial_water = partial(base_enchantement, 50, "Water")
    partial_earth = partial(base_enchantement, 50, "Earth")
    return {
        'fire': partial_fire,
        'water': partial_water,
        'earth': partial_earth
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def dispatch(spell):
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    print("Sum: " + str(spell_reducer([50, 50], "add")))
    print("Product: " + str(spell_reducer([240, 1000], "multiply")))
    print("Max: " + str(spell_reducer([10, 40], "max")))
    print("\nTesting memorized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print("\nTesting spell dispatcher...")
    dispatch: Callable = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch(None))
