def check_plant_health(plant_name, water_level, sunlight_hours) -> str:
    if plant_name is None or plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is too low "
                         "(min 1)")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is too high "
                         "(max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low "
                         "(min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too high "
                         "(max 12)")
    return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 6))
    except ValueError as ve:
        print(ve)

    print("\nTesting empty plant name...")
    try:
        print(check_plant_health(None, 5, 6))
    except ValueError as ve:
        print(ve)

    print("\nTesting bad water level...")
    try:
        print(check_plant_health("lettuce", 15, 6))
    except ValueError as ve:
        print(ve)

    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("carrots", 5, 0))
    except ValueError as ve:
        print(ve)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
