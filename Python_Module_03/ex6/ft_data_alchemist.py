import random


def players() -> dict:
    my_list = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]
    print(f"Initial list of players: {my_list}")
    res = [val.capitalize() for val in my_list]
    print(f"New list of capitalized names only: {res}")
    capital = [val for val in my_list if val == val.capitalize()]
    print(f"New list of capitalized names only: {capital}")
    scores = {x: random.randint(0, 1000) for x in res}
    print(f"Score dict: {scores}")
    average = sum(scores.values()) / len(scores)
    print()
    print(f"Score average is {round(average, 2)}")
    hight = {key: value for key, value in scores.items() if value > average}
    print(f"High scores: {hight}")
    return res


def main() -> None:
    print("=== Game Data Alchemist ===")
    players()


if __name__ == "__main__":
    main()
