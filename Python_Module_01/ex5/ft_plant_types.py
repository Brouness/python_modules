class Plant:
    def __init__(self, name: str, age: int, height: int) -> None:
        self.name = name
        self.age = age
        self.height = height


class Flower(Plant):
    def __init__(self, name: str, age: int, height: int, color: str) -> None:
        super().__init__(name, age, height)
        self.color = color
        print(f"{name} (Flower): {height}cm, {age} days, {color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name: str, age: int, height: int, diame: int) -> None:
        super().__init__(name, age, height)
        self.trunk_diameter = diame
        print(f"{name} (Tree): {height}cm, {age} days, {diame}cm diameter")

    def produce_shade(self, shade: int) -> None:
        print(f"{self.name} provides {shade} square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name: str, age: int, height: int, harvest: str) -> None:
        super().__init__(name, age, height)
        self.harvest_season = harvest
        print(f"{name} (Vegetable): {height}cm, {age} days, {harvest} harvest")
        print(f"{name} is rich in vitamine C")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===\n")
    Rose = Flower("Rose", 30, 25, "Red")
    Rose.bloom()
    Tre = Tree("Oak", 1825, 500, 50)
    Tre.produce_shade(78)
    Vegetable("Tomato", 90, 80, "summer")


if __name__ == "__main__":
    ft_plant_types()
