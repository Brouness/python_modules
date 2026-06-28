import alchemy.grimoire

name: str = "Fantasy"
ingredients = "Earth, wind and fire"
print("=== Kaboom 0 ===")
print("Using grimoire module directly")
light_spell: str = alchemy.grimoire.light_spell_record(name, ingredients)
print(f"Testing record light spell: {light_spell}")
