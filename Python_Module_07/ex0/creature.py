from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, creature_name: str, creature_type: str) -> None:
        self.name: str = creature_name
        self.creature_type: str = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"
