"""
This program defines a Plant class used to store and display basic
information about plants in a community garden.
"""


class Plant:
    """Store basic information about a garden plant."""

    def __init__(self, name, height, age_days) -> None:
        """Initialize a plant with a name, age in days, and height in cm."""
        self.name = name
        self.age_days = age_days
        self.height = height

    def plant_info(self) -> None:
        """Print a short summary of the plant's current details."""
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 30, 25)
    tulip = Plant("Tulip", 20, 15)
    Cactus = Plant("Cactus", 15, 120)

    rose.plant_info()
    tulip.plant_info()
    Cactus.plant_info()
