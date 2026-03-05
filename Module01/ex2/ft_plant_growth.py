"""Simulate a week of growth for multiple garden plants."""


class Plant:
    """Track a plant's height and age as it grows."""

    def __init__(self, name, height, age_days) -> None:
        """Initialize a plant with name, height in cm, and age in days."""
        self.name = name
        self.age_days = age_days
        self.height = height

    def grow(self) -> None:
        """Increase the plant's height by 1 cm."""
        self.height += 1

    def age(self) -> None:
        """Increase the plant's age by 1 day."""
        self.age_days += 1

    def get_info(self) -> None:
        """Print a summary of the plant's current state."""
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    print("=== Day 1 ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Tulip", 15, 20),
        Plant("Daisy", 5, 10),
    ]
    starting_heights = {}
    for plant in plants:
        starting_heights[plant.name] = plant.height
    for plant in plants:
        plant.get_info()

    print("=== Day 7 ===")
    for _ in range(6):
        for plant in plants:
            plant.grow()
            plant.age()

    for plant in plants:
        plant.get_info()
        growth = plant.height - starting_heights[plant.name]
        print(f"Growth this week: +{growth}cm")
