class Plant:
    counter: int
    counter = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        Plant.counter += 1
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def age_grow(self) -> None:
        self.age += 1


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
        ]
    for data in plant_data:
        add = Plant(data[0], data[1], data[2])
        print(f"Created: {add.name} ({add.height}cm, {add.age} days)")
    print(f"\nTotal plants created: {Plant.counter}")


if __name__ == "__main__":
    ft_plant_factory()
