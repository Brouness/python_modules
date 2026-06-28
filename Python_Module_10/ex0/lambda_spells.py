def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_list: list[dict] = sorted(artifacts,
                                     key=lambda power: power['power'],
                                     reverse=True)
    return sorted_list


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    my_list: list[dict] = list(filter(lambda m: m['power'] >= min_power,
                                      mages))
    return my_list


def spell_transformer(spells: list[str]) -> list[str]:
    my_list: list[str] = list(map(lambda element: "* " + element + " *",
                                  spells))
    return my_list


def mage_stats(mages: list[dict]) -> dict:
    max_power: int = max(mages, key=lambda m: m['power'])['power']
    min_power: int = min(mages, key=lambda m: m['power'])['power']
    total: list[int] = list(map(lambda m: m['power'], mages))
    average = round(sum(total) / len(total), 2)
    all_values: dict = {'max_power': max_power, 'min_power': min_power,
                        'avg_power': average}
    return all_values


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    my_dic = [{'name': 'Fire Staff', 'power': 92},
              {'name': 'Crystal Orb', 'power': 85},
              ]
    my_list: list = artifact_sorter(my_dic)
    print(f"{my_list[0]['name']} ({my_list[0]['power']} power)"
          f" comes before {my_list[1]['name']} ({my_list[1]['power']} power)")
    print("\nTesting spell transformer...")
    spells: list = spell_transformer(["fireball", "heal", "shield"])
    print(f"{spells[0]} {spells[1]} {spells[2]}")
    print("\nTesting power filter...")
    mages = [
        {'name': 'Alex', 'power': 90, 'element': 'fire'},
        {'name': 'Jordan', 'power': 40, 'element': 'water'},
        {'name': 'Riley', 'power': 75, 'element': 'earth'},
    ]
    filtered = power_filter(mages, 70)
    print(f"Mages with power >= 70: {[m['name'] for m in filtered]}")
    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max: {stats['max_power']}, "
          f"Min: {stats['min_power']}, Avg: {stats['avg_power']}")
