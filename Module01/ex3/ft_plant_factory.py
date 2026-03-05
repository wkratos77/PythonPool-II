"""Plant Factory: Create multiple plant instances and track total created."""


class Plant:
    """Represent a plant instance and track total created."""

    plant_count = 0

    def __init__(self, name, height, age_days) -> None:
        """Initialize a plant and increment the factory count."""
        self.name = name
        self.age_days = age_days
        self.height = height
        Plant.plant_count += 1

    def get_info(self) -> None:
        """Print a summary string for the plant."""
        print(f"Created: {self.name} ({self.height}cm, {self.age_days} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    for plant in plants:
        plant.get_info()
    print(f"\nTotal plants created: {Plant.plant_count}")
