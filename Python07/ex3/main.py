from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    engine.hand = [
        factory.create_creature("dragon"),
        factory.create_creature("goblin"),
        factory.create_spell("lightning"),
    ]
    engine.cards_created = len(engine.hand)

    engine.battlefield = [
        "Enemy Player",
    ]

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Supported types:", factory.get_supported_types())
    print("\nSimulating aggressive turn...")
    hand_str = ", ".join(f"{card.name} ({card.cost})" for card in engine.hand)
    print("Hand:", hand_str)

    print("\nTurn execution:")
    print("Strategy:", strategy.get_strategy_name())
    result = engine.simulate_turn()
    status = engine.get_engine_status()

    print("Actions:", result["actions"])
    print()
    print("Game Report:")
    print(status)
    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")
