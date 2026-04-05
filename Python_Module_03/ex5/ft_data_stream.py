import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = [
        "alice",
        "bob",
        "dylan",
        "charlie"
    ]
    actions = [
        "run",
        "sleep",
        "eat",
        "move",
        "climb",
        "swim",
        "grab",
        "release"
    ]
    while True:
        yield random.choice(players), random.choice(actions)


def consume_event(my_list: list):
    while my_list:
        choice = random.choice(my_list)
        my_list.remove(choice)
        yield choice


def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        player, action = next(gen)
        print(f"Event {i}: Player  {player} did action {action}")
    mylist = []
    number_of_actions = 10
    for i in range(number_of_actions):
        mylist.append(next(gen))
    print(f"Built list of {number_of_actions} events: {mylist}")
    generator = consume_event(mylist)
    while mylist:
        print(f"Got event from list: {next(generator)}")
        print(f"Remains in list: {mylist}")


if __name__ == "__main__":
    main()
