from ex2.EliteCard import EliteCard


if __name__ == "__main__":
    print("=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    print("Playing Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    attacker = EliteCard("Arcane Warrior", 5, "Epic", 5, 3, 10, 8, 4)
    Enemy = EliteCard("Enemy", 2, "Common", 2, 1, 5, 0, 0)
    print("Attack result:", attacker.attack(Enemy))
    print("Defend result:", attacker.defend(5))
    print()

    print("Magic phase:")
    Enemy1 = EliteCard("Enemy1", 3, "Uncommon", 3, 2, 6, 0, 0)
    Enemy2 = EliteCard("Enemy2", 4, "Rare", 4, 3, 8, 0, 0)
    print("Spell cast:", attacker.cast_spell("Fireball", [Enemy1, Enemy2]))
    print("Mana channel:", attacker.channel_mana(3))
    print()

    print("Multiple interface implementation successful!")
