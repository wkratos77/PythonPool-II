from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, int):
            return CreatureCard('Warrior', 3, 'Common', name_or_power, 5)

        if name_or_power == 'dragon':
            return CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
        elif name_or_power == 'goblin':
            return CreatureCard('Goblin Warior', 2, 'Mythic', 5, 1)
        return CreatureCard('Cute Unicorn', 1, 'Banal', 1, 1)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, int):
            return SpellCard('Fireball', 2, 'Rare',
                             f'deal {name_or_power} damage')

        if name_or_power == 'lightning':
            return SpellCard('Lightning Bolt', 3, 'Rare', 'damage')
        elif name_or_power == 'fire':
            return SpellCard('Fireball', 2, 'Rare', 'damage')
        elif name_or_power == 'ice':
            return SpellCard('Ice arrow', 4, 'More than rare', 'damage')
        return SpellCard('Cotton bubble', 1, 'Banal', 'heal')

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, int):
            return ArtifactCard('Mana Ring', 4, 'Epic',
                                name_or_power, 'damage')

        if name_or_power == 'mana' or name_or_power == 'mana_ring':
            return ArtifactCard('mana_ring', 4, 'Epic', 4, 'damage')
        return ArtifactCard('Ancient book', 1, 'Common', 4, 'heal')

    def create_themed_deck(self, size: int) -> dict:
        types = ['dragon', 'goblin', 'lightning', 'fireball', 'ice',
                 'mana_ring']
        deck = {}

        if size > len(types):
            size = len(types)
        for i in range(size):
            t = types[i]
            if t in ['dragon', 'goblin']:
                card = self.create_creature(t)
            elif t == 'mana_ring':
                card = self.create_artifact(t)
            else:
                card = self.create_spell(t)

            deck[f'card{i + 1}'] = card
        return deck

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
