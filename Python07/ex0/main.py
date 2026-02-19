from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    creature_card = CreatureCard("Fire Dragon", 5, "legendary", 7, 5)
    print(creature_card.get_card_info())
    print()
    print("Playing Fire Dragon with "
          "6 mana available:")
    print("Playable:", creature_card.is_playable(6))
    print("Play result: " + str(creature_card.play({})))
    print()
    print("Fire Dragon attacks Goblin Warrior:")
    goblin_card = CreatureCard("Goblin Warrior", 2, "Common", 3, 4)
    attack_result = creature_card.attack_target(goblin_card)
    print("Attack result:", attack_result)
    print()
    print("Testing insufficient mana (3 available):")
    print("Playable:", creature_card.is_playable(3))
    print()
    print("Abstract pattern successfully demonstrated!")
