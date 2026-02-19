from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        try:
            self.attack = int(attack)
            self.health = int(health)
            if self.attack <= 0 or self.health <= 0:
                raise ValueError("Attack and health must be positive.")
        except ValueError as e:
            print(f"Error creating CreatureCard: {e}")
            self.attack = max(0, int(attack))
            self.health = max(0, int(health))

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'}

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return card_info

    def attack_target(self, target) -> dict:
        target.health -= self.attack
        if target.health < 0:
            dead = True
            target.health = 0
        else:
            dead = False
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": dead
        }
