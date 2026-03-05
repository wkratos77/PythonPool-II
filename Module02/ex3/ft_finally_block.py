def water_plants(plant_list) -> None:
    print("Opening watering system...")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as te:
        print(f"Error: {te}")
        return
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!\n")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)

    print("Testing with error...")
    plants_with_none = ["tomato", None, "carrots"]
    water_plants(plants_with_none)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
