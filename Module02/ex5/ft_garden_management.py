class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant) -> None:
        if plant is None or plant == "":
            raise PlantError(
                "Error adding plant: Plant name cannot be empty!"
            )
        self.plants.append(plant)
        print(f"Added {plant} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant is None:
                    raise WaterError("Cannot water None - invalid plant!")
                print(f"Watering {plant} - success")
        except WaterError as we:
            print(f"Error: {we}")
            return
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self, plant_name, water_level, sunlight_hours
    ) -> None:
        if plant_name is None or plant_name == "":
            raise PlantError(
                "Error adding plant: Plant name cannot be empty!"
            )
        if water_level < 1:
            raise WaterError(
                f"Error checking {plant_name}: "
                f"Water level {water_level} is too low (min 1)"
            )
        if water_level > 10:
            raise WaterError(
                f"Error checking {plant_name}: "
                f"Water level {water_level} is too high (max 10)"
            )
        if sunlight_hours < 2:
            raise PlantError(
                f"Error checking {plant_name}: "
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        if sunlight_hours > 12:
            raise PlantError(
                f"Error checking {plant_name}: "
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        print(
            f"{plant_name}: healthy "
            f"(water: {water_level}, sun: {sunlight_hours})"
        )

    def check_tank(self) -> None:
        raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    print()

    manager = GardenManager()
    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    try:
        manager.add_plant("")
    except PlantError as pe:
        print(pe)
    print()

    print("Watering plants...")
    manager.water_plants()
    print()

    print("Checking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
        manager.check_plant_health("lettuce", 15, 8)
    except GardenError as ge:
        print(ge)
    print()

    print("Testing error recovery...")
    try:
        manager.check_tank()
    except GardenError as ge:
        print(f"Caught GardenError: {ge}")
        print("System recovered and continuing...")

    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
