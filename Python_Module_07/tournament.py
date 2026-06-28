from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def battle(batlle_factory: list[tuple]) -> None:
    print("*** Tournament ***")
    print(f"\n{len(batlle_factory)} opponents involved")
    for i in range(len(batlle_factory)):
        for j in range(i + 1, len(batlle_factory)):
            print("\n* Battle *")
            opponent_1 = batlle_factory[i][0].create_base()
            opponent_2 = batlle_factory[j][0].create_base()
            print(opponent_1.describe())
            print(" vs.")
            print(opponent_2.describe())
            opponent_1_strategy = batlle_factory[i][1]
            opponent_2_strategy = batlle_factory[j][1]
            print(" now fight!")
            try:

                opponent_1_strategy.act(opponent_1)
                opponent_2_strategy.act(opponent_2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    mytuple1t1 = (FlameFactory(), NormalStrategy())
    mytuple2t1 = (HealingCreatureFactory(), DefensiveStrategy())
    battle_factory1 = [mytuple1t1, mytuple2t1]
    battle(battle_factory1)
    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    mytuple1t2 = (FlameFactory(), AggressiveStrategy())
    mytuple2t2 = (HealingCreatureFactory(), DefensiveStrategy())
    battle_factory2 = [mytuple1t2, mytuple2t2]
    battle(battle_factory2)
    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    mytuple1t3 = (AquaFactory(), NormalStrategy())
    mytuple2t3 = (HealingCreatureFactory(), DefensiveStrategy())
    mytuple3t3 = (TransformCreatureFactory(), AggressiveStrategy())
    battle_factory3 = [mytuple1t3, mytuple2t3, mytuple3t3]
    battle(battle_factory3)


if __name__ == "__main__":
    main()
