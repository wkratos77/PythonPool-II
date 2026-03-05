from ex0.Card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            card = self.cards[0]
            self.cards.pop(0)
            return card
        raise IndexError("Deck is empty. Cannot draw a card.")

    def get_deck_stats(self) -> dict:
        total_cost = sum(card.cost for card in self.cards)
        avg_cost = total_cost / len(self.cards) if self.cards else 0
        stats = {
            'total_cards': len(self.cards),
            'creatures': sum(1 for card in self.cards
                             if 'Creature' in card.__class__.__name__),
            'spells': sum(1 for card in self.cards
                          if 'Spell' in card.__class__.__name__),
            'artifacts': sum(1 for card in self.cards
                             if 'Artifact' in card.__class__.__name__),
            'avg_cost': round(avg_cost, 1)
        }
        return stats
