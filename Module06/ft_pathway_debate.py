import alchemy.transmutation


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(
        "lead_to_gold(): "
        f"{alchemy.transmutation.lead_to_gold()}"
    )
    print(
        "stone_to_gem(): "
        f"{alchemy.transmutation.stone_to_gem()}\n"
    )

    print("Testing Relative Imports (from advanced.py):")
    print(
        "philosophers_stone(): "
        f"{alchemy.transmutation.philosophers_stone()}"
    )
    print(
        "elixir_of_life(): "
        f"{alchemy.transmutation.elixir_of_life()}\n"
    )

    print("Testing Package Access:")
    print(
        "alchemy.transmutation.lead_to_gold(): "
        f"{alchemy.transmutation.lead_to_gold()}"
    )
    print(
        "alchemy.transmutation.philosophers_stone(): "
        f"{alchemy.transmutation.philosophers_stone()}\n"
    )

    print("Both pathways work! Absolute: clear, Relative: concise")
