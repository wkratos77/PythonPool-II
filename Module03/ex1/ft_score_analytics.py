import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
        sys.exit()

    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid score: {arg}. Please provide numeric values only.")
            sys.exit()

    total_players = len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    average_score = sum(scores) / total_players

    print("Scores processed:", scores)
    print(f"Total players: {total_players}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {average_score:.1f}")
    print(f"High score: {highest_score}")
    print(f"Low score: {lowest_score}")
    print(f"Score range: {highest_score - lowest_score}")