def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    validation_result = validate_ingredients(ingredients)
    if validation_result == f"{ingredients} - INVALID":
        return f"Spell rejected: {spell_name} ({validation_result})"
    else:
        return f"Spell recorded: {spell_name} ({validation_result})"
