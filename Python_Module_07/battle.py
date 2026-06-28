from ex0 import FlameFactory, AquaFactory


def test_factory(factory) -> None:
    print("Testing factory")
    factory_base = factory.create_base()
    factory_evolved = factory.create_evolved()
    print(factory_base.describe())
    print(factory_base.attack())
    print(factory_evolved.describe())
    print(factory_evolved.attack())


def test_battle(factory1, factory2) -> None:
    print("Testing battle")
    factory1_base = factory1.create_base()
    factory2_base = factory2.create_base()
    print(factory1_base.describe())
    print("vs.")
    print(factory2_base.describe())
    print("fight!")
    print(factory1_base.attack())
    print(factory2_base.attack())


def main() -> None:
    flameling = FlameFactory()
    aqua = AquaFactory()
    test_factory(flameling)
    print()
    test_factory(aqua)
    print()
    test_battle(flameling, aqua)


if __name__ == "__main__":
    main()
