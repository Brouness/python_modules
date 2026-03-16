class Plant:
    def __init__(self, name: str, height: int, Age: int) -> None:
        self.name = name
        self.height = height
        self.Age = Age

    def grow(self) -> None:
        self.height += 6

    def age(self) -> None:
        self.Age += 6

    def get_info(self) -> None:
        return print(f"Growth this week: +{6}cm")


def ft_plant_growth() -> None:
    Rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(f"{Rose.name}: {Rose.height}cm, {Rose.Age} days old")
    print("=== Day 7 ===")
    Rose.grow()
    Rose.age()
    print(f"{Rose.name}: {Rose.height}cm, {Rose.Age} days old")
    Rose.get_info()


if __name__ == "__main__":
    ft_plant_growth()
