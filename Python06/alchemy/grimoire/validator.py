def validate_ingredients(ingredients: str) -> str:
    allowed = {"fire", "water", "earth", "air"}
    words = ingredients.split()
    for word in words:
        if word in allowed:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
