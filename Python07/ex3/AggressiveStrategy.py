from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana_budget = 5
        damage = 0
        targets = self.prioritize_targets(battlefield)
        played = []
        for c in sorted(hand, key=lambda x: x.cost):
            if c.cost <= mana_budget:
                played.append(c)
                mana_budget -= c.cost
        for card in played:
            damage += getattr(card, "attack", 0)

        return {
            'cards_played': [card.name for card in played],
            'mana_used': sum(card.cost for card in played),
            'targets_attacked': targets,
            'damage_dealt': damage
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        targets = []
        for target in available_targets:
            t = target.lower()
            if "player" in t:
                targets.append(target)
            if "creature" in t:
                targets.append(target)
        return targets
