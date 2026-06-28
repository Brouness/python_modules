def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    validate = validate_ingredients(ingredients)
    if "VALID" in validate:
        return f"Spell recorded: {spell_name} ({validate})"
    else:
        return f"Spell rejected: {spell_name} ({validate})"
