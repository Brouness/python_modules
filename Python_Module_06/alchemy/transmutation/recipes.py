from alchemy.elements import create_air
from ..potions import strenght_potion, create_fire


def lead_to_gold() -> str:
    air: str = create_air()
    potion: str = strenght_potion()
    fire: str = create_fire()
    return (f"Recipe transmuting Lead to Gold: brew '{air}' "
            f"and '{potion}' mixed with '{fire}'"
            )
