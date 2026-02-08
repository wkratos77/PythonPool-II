from alchemy.grimoire import record_spell, validate_ingredients

if __name__ == "__main__":
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print('validate_ingredients("fire air"): '
          f'{validate_ingredients("fire air")}')
    print('validate_ingredients("dragon scales"): '
          f'{validate_ingredients("dragon scales")}\n')

    print("Testing spell recording with validation:")
    print('record_spell("Flame Burst", "fire air"): '
          f'{record_spell("Flame Burst", "fire air")}')
    print('record_spell("Forbidden Ritual", "dragon scales"): '
          f'{record_spell("Forbidden Ritual", "dragon scales")}\n')

    print("Testing late import technique:")
    print("Validator is imported inside record_spell() "
          "to avoid circular imports.")

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
