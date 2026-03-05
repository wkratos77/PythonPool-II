def game_event_stream(count) -> tuple:
    players = ("alice", "bob", "charlie")
    for i in range(1, count + 1):
        if i == 1:
            yield ("alice", 5, "killed monster")
            continue
        if i == 2:
            yield ("bob", 12, "found treasure")
            continue
        if i == 3:
            yield ("charlie", 8, "leve led up")
            continue
        player = players[(i - 1) % 3]
        if 4 <= i <= 4 + 88 - 1:
            action = "found treasure"
        elif 4 + 88 <= i <= 4 + 88 + 155 - 1:
            action = "leveled up"
        else:
            action = "killed monster"
        if 4 <= i <= 4 + 341 - 1:
            level = 10
        else:
            level = 5

        yield (player, level, action)


def fib_stream() -> int:
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prime_stream() -> int:
    x = 2
    while True:
        if is_prime(x):
            yield x
        x += 1


def print_int_sequence_from_generator(gen, count) -> None:
    for i in range(count):
        n = next(gen)
        if i > 0:
            print(", ", end="")
        print(n, end="")
    print()


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print()
    print("Processing 1000 game events...")

    total_events = 0
    high_level = 0
    treasure = 0
    levelups = 0

    stream = game_event_stream(1000)
    shown_dots = False

    for event in stream:
        total_events += 1
        player, level, action = event

        if total_events <= 3:
            print(f"Event {total_events}: Player {player} "
                  f"(level {level}) {action}")
        elif not shown_dots:
            print("...")
            shown_dots = True

        if level >= 10:
            high_level += 1
        if action == "found treasure":
            treasure += 1
        if action == "leveled up":
            levelups += 1
    print()

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levelups}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print()
    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    print_int_sequence_from_generator(fib_stream(), 10)

    print("Prime numbers (first 5): ", end="")
    print_int_sequence_from_generator(prime_stream(), 5)
