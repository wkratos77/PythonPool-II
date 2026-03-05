if __name__ == "__main__":
    player_scores = {
        'alice': 2300,
        'bob': 1800,
        'charlie': 2150,
        'diana': 2400,
    }
    player_achievements = {
        'alice': {'first_kill', 'level_10', 'treasure_hunter'},
        'charlie': {'level_10', 'boss_slayer', 'speed_demon'},
        'bob': set(),
        'diana': {'first_kill', 'collector', 'speed_demon', 'perfectionist'},
    }
    player_regions = {
        'alice': 'north',
        'bob': 'east',
        'charlie': 'east',
        'diana': 'central',
    }
    print("=== Game Analytics Dashboard ===")
    print()

    print("=== List Comprehension Examples ===")
    high_scorers = [
        name for name, score in player_scores.items() if score > 2000
        ]
    print("High scorers (>2000):", high_scorers)
    print("Scores doubled:", [score * 2 for score in player_scores.values()])
    active_players = [name for name, achs in player_achievements.items()
                      if len(achs) > 0]
    print("Active players:", active_players)
    print()

    print("=== Dict Comprehension Examples ===")
    print("Player scores:", player_scores)
    score_categories = {
        "high": sum([1 for s in player_scores.values() if s > 2000]),
        "medium": sum([1 for s in player_scores.values() if s >= 1500
                       and s <= 2000]),
        "low": sum([1 for s in player_scores.values() if s < 1500]),
    }
    print("Score categories:", score_categories)
    achievement_counts = {name: len(achs) for name, achs
                          in player_achievements.items()}
    print("Achievement counts:", achievement_counts)
    print()

    print("=== Set Comprehension Examples ===")
    print("Unique players:", set(player_scores.keys()))
    unique_achievements = {
        ach for achs in player_achievements.values() for ach in achs
    }
    print("Unique achievements:", unique_achievements)
    active_regions = {region for name, region in player_regions.items()
                      if name in active_players}
    print("Active regions:", active_regions)
    print()

    print("=== Combined Analysis ===")
    total_players = len(player_scores)
    total_unique_achievements = len(unique_achievements)
    avg_score = sum(player_scores.values()) / total_players
    top_performer = max(player_scores, key=player_scores.get)
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {avg_score:.1f}")
    print(f"Top performer: {top_performer} "
          f"({player_scores[top_performer]} points), "
          f"{len(player_achievements[top_performer])} achievements")
