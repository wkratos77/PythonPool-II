from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = []
        self.battlefield = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def simulate_turn(self) -> dict:
        if self.strategy is None or self.factory is None:
            raise ValueError("Engine not configured")
        self.turns_simulated += 1
        actions = self.strategy.execute_turn(self.hand, self.battlefield)
        self.total_damage += actions.get("damage_dealt", 0)
        return {
            'strategy': self.strategy.get_strategy_name(),
            'actions': actions
        }

    def get_engine_status(self) -> dict:
        if self.strategy is None:
            strategy_name = None
        else:
            strategy_name = self.strategy.get_strategy_name()
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
            "supported_types": (self.factory.get_supported_types()
                                if self.factory else None),
        }
