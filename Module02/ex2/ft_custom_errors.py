class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as pe:
        print(f"Caught PlantError: {pe}\n")
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as we:
        print(f"Caught WaterError: {we}\n")
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as ge:
        print(f"Caught GardenError: {ge}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as ge:
        print(f"Caught GardenError: {ge}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
