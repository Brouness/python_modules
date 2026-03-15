class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> str:
        self.height += 1
        return f"{self.name} grew 1cm"

    def description(self) -> str:
        return f"{self.name}: {self.height}cm"

    def category(self) -> str:
        return "Plant"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def bloom(self) -> str:
        return f"{self.color} flowers (blooming)"

    def description(self) -> str:
        return f"{self.name}: {self.height}cm, {self.bloom()}"

    def category(self) -> str:
        return "FloweringPlant"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize

    def description(self) -> str:
        string = f"{self.height}cm, {self.bloom()}"
        flake = f", Prize points: {self.prize_points}"
        return f"{self.name}: {string}{flake}"

    def category(self) -> str:
        return "PrizeFlower"


class GardenManager:

    class GardenStats:
        def __init__(self, plants: list) -> None:
            self.plants = plants

        def count_plants(self) -> int:
            count = 0
            for plant in self.plants:
                count += 1
            return count

        def total_growth(self) -> int:
            count = 0
            for plant in self.plants:
                count += 1
            return count

        def count_type(self) -> dict:
            regular = 0
            flowering = 0
            prize = 0
            for plant in self.plants:
                if plant.category() == "Plant":
                    regular += 1
                elif plant.category() == "FloweringPlant":
                    flowering += 1
                elif plant.category() == "PrizeFlower":
                    prize += 1
            return {
                "regular": regular,
                "flowering": flowering,
                "prize": prize
            }

    def __init__(self) -> None:
        self.gardens = {
            "Alice": [],
            "Bob": []
        }

    def add_plant(self, garden_name: str, plant: Plant) -> str:
        self.gardens[garden_name].append(plant)
        return f"Added {plant.name} to {garden_name}'s garden"

    def grow_garden(self, garden_name: str) -> None:
        print(f"\n{garden_name} is helping all plants grow...")
        for plant in self.gardens[garden_name]:
            print(plant.grow())

    def garden_report(self, garden_name: str) -> None:
        print(f"\n=== {garden_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.gardens[garden_name]:
            print(f"- {plant.description()}")

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    @classmethod
    def create_garden_network(cls):
        return cls()

    def garden_score(self, garden_name: str) -> int:
        score = 0
        for plant in self.gardens[garden_name]:
            score += plant.height
            if plant.category() == "PrizeFlower":
                score += plant.prize_points
        return score

    def total_gardens(self) -> int:
        total = 0
        for garden in self.gardens:
            total += 1
        return (total)


def ft_garden_analytics() -> None:
    youness = GardenManager.create_garden_network()
    tree = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    print("=== Garden Management System Demo ===\n")
    print(youness.add_plant("Alice", tree))
    print(youness.add_plant("Alice", rose))
    print(youness.add_plant("Alice", sunflower))
    youness.grow_garden("Alice")
    youness.garden_report("Alice")
    stats = GardenManager.GardenStats(youness.gardens["Alice"])
    print(
        f"Plants added: "
        f"{stats.count_plants()}, Total growth: {stats.total_growth()}cm"
    )
    distribution = stats.count_type()
    print(
        f"Plant types: "
        f"{distribution['regular']} regular, "
        f"{distribution['flowering']} flowering, "
        f"{distribution['prize']} prize flowers"
    )
    print("Height validation test:", GardenManager.validate_height(10))
    alice_score = youness.garden_score("Alice")
    bob_score = youness.garden_score("Bob")
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {youness.total_gardens()}")


if __name__ == "__main__":
    ft_garden_analytics()
