from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = dark_spell_allowed_ingredients()
    for allowed in allowed_ingredients:
        if allowed in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
