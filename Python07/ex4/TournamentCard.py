from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 card_id: str, rating: int, wins: int, losses: int):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.rating = rating
        self.wins = wins
        self.losses = losses

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Tournament card deployed'
        }

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.cost * 2,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.cost, incoming_damage)
        taken = incoming_damage - blocked
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': blocked,
            'still_alive': True
        }

    def get_combat_stats(self) -> dict:
        return {
            'card_name': self.name,
            'attack_power': self.cost * 2,
            'defense_power': self.cost
        }

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def calculate_rating(self) -> int:
        return self.rating

    def get_rank_info(self) -> dict:
        return {
            'card_name': self.name,
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            'card_id': self.card_id,
            'card_name': self.name,
            'rarity': self.rarity,
            'rating': self.rating,
            'record': f"{self.wins}-{self.losses}"
        }
