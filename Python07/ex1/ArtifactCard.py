from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        self.effect = effect
        try:
            self.durability = int(durability)
            if self.durability <= 0:
                raise ValueError("Durability must be positive.")
        except ValueError as e:
            print(f"Error creating ArtifactCard: {e}")
            self.durability = max(0, int(durability))

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }

    def activate_ability(self) -> dict:
        return {
            'card': self.name,
            'ability': self.effect,
            'durability': self.durability
        }
