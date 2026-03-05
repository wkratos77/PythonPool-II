def check_temperature(temp_str: str) -> str:
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number")

    if temp < 0:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")
    else:
        return f"Temperature {temp}°C is perfect for plants!"


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    try:
        print(check_temperature("25"))
    except ValueError as e:
        print(e)

    print("\nTesting temperature: abc")
    try:
        print(check_temperature("abc"))
    except ValueError as e:
        print(e)
    print("\nTesting temperature: 100")
    try:
        print(check_temperature("100"))
    except ValueError as e:
        print(e)
    print("\nTesting temperature: -50")
    try:
        print(check_temperature("-50"))
    except ValueError as e:
        print(e)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
