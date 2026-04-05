import random


def gen_player_achievements(number: int) -> set:
    all_achievement = [
        "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
        "Survivor",
        "Master Explorer", "Treasure Hunter", "Unstoppable", "First Steps",
        "Collector Supreme",
        "Untouchable", "Sharp Mind", "Boss Slayer"
    ]
    picked = random.sample(all_achievement, number)
    return set(picked)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    number = random.randint(4, 13)
    alice = gen_player_achievements(number)
    bob = gen_player_achievements(number)
    charlie = gen_player_achievements(number)
    dylan = gen_player_achievements(number)
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    all_achievement = set.union(bob, alice, charlie, dylan)
    print(f"All distinct achievements: {all_achievement}")
    print()
    common = set.intersection(alice, bob, charlie, dylan)
    print(f"Comon achievements: {common}")
    print()
    print(f"Only Alice has: {alice - (bob | charlie | dylan)}")
    print(f"Only Bob has: {bob - (alice | charlie | dylan)}")
    print(f"Only Charlie has: {charlie - (alice | bob | dylan)}")
    print(f"Only Dylan has: {dylan - (alice | bob | charlie)}")
    print()
    print(f"Alice is missing: {all_achievement - alice}")
    print(f"Bob is missing: {all_achievement - bob}")
    print(f"Charlie is missing: {all_achievement - charlie}")
    print(f"Dylan is mising: {all_achievement - dylan}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Caught an Error: {e}")
