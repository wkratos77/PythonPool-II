from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    platform = TournamentPlatform()

    card1 = TournamentCard("Fire Dragon", 5, "Epic", "dragon_001", 1200, 0, 0)
    card2 = TournamentCard("Ice Wizard", 4, "Rare", "wizard_001", 1150, 0, 0)
    card3 = TournamentCard("Forest Guardian", 3, "Common", "FG003", 800, 5, 10)

    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    platform.register_card(card1)
    platform.register_card(card2)
    platform.register_card(card3)
    info = card1.get_card_info()
    print(f"{info['name']} (ID: {card1.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {card1.rating}")
    print(f"- Record: {card1.wins}-{card1.losses}")
    print()

    info = card2.get_card_info()
    print(f"{info['name']} (ID: {card2.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {card2.rating}")
    print(f"- Record: {card2.wins}-{card2.losses}")
    print()
    print("Creating tournament match...")
    print("Match result:", platform.create_match("dragon_001", "wizard_001"))
    print()

    print("Tournament Leaderboard::")
    for entry in platform.get_leaderboard():
        print(entry)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
