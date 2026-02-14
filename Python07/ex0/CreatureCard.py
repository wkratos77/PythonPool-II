from Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        try:
            self.attack = int(attack)
            self.health = int(health)
            if self.attack < 0 or self.health < 0:
                raise ValueError("Attack and health must be non-negative.")
        except ValueError as e:
            print(f"Error creating CreatureCard: {e}")
            self.attack = max(0, int(attack))
            self.health = max(0, int(health))

    def play(self, game_state: dict) -> dict:
        return game_state

    def attack_target(self, target) -> dict:
        target.health -= self.attack
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": target.health
        }
