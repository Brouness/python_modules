from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    earth: str = create_earth()
    air: str = create_air()
    return f"Healing potion brewed with '{earth}' and '{air}'"


def strenght_potion() -> str:
    fire: str = create_fire()
    water: str = create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"
