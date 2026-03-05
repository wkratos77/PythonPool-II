import math

if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    origin = (0, 0, 0)
    pos = (10, 20, 5)
    print("Position created:", pos)
    x1, y1, z1 = origin
    x2, y2, z2 = pos
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    d = math.sqrt(dx * dx + dy * dy + dz * dz)
    print(f"Distance between {origin} and {pos}: {d:.2f}")
    s = "3,4,0"
    print()
    print(f'Parsing coordinates: "{s}"')
    parts = s.split(",")
    parsed = (int(parts[0]), int(parts[1]), int(parts[2]))
    print(f"Parsed position: {parsed}")
    x1, y1, z1 = origin
    x2, y2, z2 = parsed
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    d = math.sqrt(dx * dx + dy * dy + dz * dz)
    print(f"Distance between {origin} and {parsed}: {d:.1f}")
    s = "abc,def,ghi"
    print()
    print(f'Parsing invalid coordinates: "{s}"')
    try:
        parts = s.split(",")
        invparsed = (int(parts[0]), int(parts[1]), int(parts[2]))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    print()
    print("Unpacking demonstration:")
    print(f"Player at x={x2}, y={y2}, z={z2}")
    print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")
