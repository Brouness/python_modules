from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_creature_base(creature) -> None:
    print(" base:")
    healing_creature = creature.create_base()
    print(healing_creature.describe())
    print(healing_creature.attack())
    print(healing_creature.heal())


def test_healing_creature_evolved(creature) -> None:
    print(" evolved:")
    healing_creature = creature.create_evolved()
    print(healing_creature.describe())
    print(healing_creature.attack())
    print(healing_creature.heal())


def test_transform_creature_base(creature) -> None:
    print(" base:")
    transform_creature = creature.create_base()
    print(transform_creature.describe())
    print(transform_creature.attack())
    print(transform_creature.transform())
    print(transform_creature.attack())
    print(transform_creature.revert())


def test_transform_creature_evolved(creature) -> None:
    print(" evolved:")
    transform_creature = creature.create_evolved()
    print(transform_creature.describe())
    print(transform_creature.attack())
    print(transform_creature.transform())
    print(transform_creature.attack())
    print(transform_creature.revert())


def main() -> None:
    sproutling = HealingCreatureFactory()
    print("Testing Creature with healing capability")
    test_healing_creature_base(sproutling)
    test_healing_creature_evolved(sproutling)
    print()
    print("Testing Creature with transform capability")
    shiftling = TransformCreatureFactory()
    test_transform_creature_base(shiftling)
    test_transform_creature_evolved(shiftling)


if __name__ == "__main__":
    main()
