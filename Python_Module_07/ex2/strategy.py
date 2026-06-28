from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature) -> None:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        if isinstance(creature, Creature):
            return True
        else:
            return False

    def act(self, creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise Exception(
                f"Invalid Creature '{creature.name}' for this normal strategy"
                )


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        else:
            return False

    def act(self, creature) -> None:
        if self.is_valid(creature):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise Exception(
                f"Invalid Creature '{creature.name}' f" +
                "or this aggressive strategy"
                )


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        else:
            return False

    def act(self, creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            raise Exception(
                f"Invalid Creature '{creature.name}' for " +
                "this Defensive strategy"
                )
