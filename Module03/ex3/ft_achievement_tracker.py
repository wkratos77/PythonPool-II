if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
    }

    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)
    print()

    print("=== Achievement Analytics ===")
    unique = alice.union(bob).union(charlie)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")
    print()

    common = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common}")
    alice_only = alice.difference(bob.union(charlie))
    bob_only = bob.difference(alice.union(charlie))
    charlie_only = charlie.difference(alice.union(bob))
    rare = alice_only.union(bob_only).union(charlie_only)
    print(f"Rare achievements (1 player): {rare}")
    print()

    alice_bob_common = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")
    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")
    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")
