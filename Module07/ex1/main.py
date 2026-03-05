from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")
    deck = Deck()
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common",
                            "Deal 3 damage to target"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Uncommon", 5,
                               "Permanent: +1 mana per turn"))
    deck.add_card(CreatureCard("Fire Dragon", 5, "Common", 8, 5))
    print("Building deck with different card types...")
    print("Deck stats:", deck.get_deck_stats())
    print("\nDrawing and playing cards:")
    card = deck.draw_card()
    print(f"\nDrew: {card.name} ({card.__class__.__name__})")
    print("Play result:", card.play({}))
    card = deck.draw_card()
    print(f"\nDrew: {card.name} ({card.__class__.__name__})")
    print("Play result:", card.play({}))
    card = deck.draw_card()
    print(f"\nDrew: {card.name} ({card.__class__.__name__})")
    print("Play result:", card.play({}))
    print()
    print("Polymorphism in action: Same interface, different card behaviors!")
