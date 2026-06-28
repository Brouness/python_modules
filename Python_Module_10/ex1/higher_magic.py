from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power}"


def heal(target: str, power: int) -> str:
    return f"Heals {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"shield defence {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine(target: str, power: int) -> tuple:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def condition(target: str, power: int) -> bool:
    if target == target.capitalize() and power >= 10:
        return True
    return False


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return cast_all


def main() -> None:
    print("\nTesting spell combiner...")
    combine = spell_combiner(fireball, heal)
    fire_bal = combine("Dragon", 10)[0]
    heals = combine("Dragon", 10)[1]
    print(f"{fire_bal}, {heals}")
    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print("Original: " + fireball("Dargon", 10)[25:] + ", " +
          "Amplified: " + mega_fireball("Dragon", 10)[25:])
    print("\nTesting conditional cast...")
    caster = conditional_caster(condition, fireball)
    print(caster("Dragon", 10))
    print("\nTesting spell sequence...")
    spells = [fireball, heal, shield]
    spells_sequence = spell_sequence(spells)
    spells = spells_sequence("Dragon", 12)
    for spell in spells:
        print(spell)


if __name__ == "__main__":
    main()
