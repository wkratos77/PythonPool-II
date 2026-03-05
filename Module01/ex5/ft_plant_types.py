"""
This module defines a base Plant class and specialized plant types:
Flower, Tree, and Vegetable. It demonstrates inheritance and reuse
of common plant attributes while adding specialized behaviors.
"""


class Plant:
    """Base class representing common plant features."""

    def __init__(self, name, height, age_days) -> None:
        """Initialize a plant with a name, height (cm), and age (days)."""
        self.name = name
        self.height = height
        self.age_days = age_days

    def get_info(self) -> str:
        """Return a base summary string for the plant."""
        return f"{self.name}: {self.height}cm, {self.age_days} days"


class Flower(Plant):
    """A plant type that has a color and can bloom."""

    def __init__(self, name, height, age_days, color) -> None:
        """Initialize a flower with common plant data plus a color."""
        super().__init__(name, height, age_days)
        self.color = color

    def get_info(self) -> str:
        """Return a summary string including flower-specific details."""
        base = super().get_info()
        return f"{base}, {self.color} color"

    def bloom(self) -> str:
        """Return a message describing the flower blooming."""
        return f"{self.name} is blooming beautifully!\n"


class Tree(Plant):
    """A plant type that has a trunk diameter and can produce shade."""

    def __init__(self, name, height, age_days, trunk_diameter) -> None:
        """Initialize a tree with common plant data plus trunk diameter(cm)."""
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> str:
        """Return a summary string including tree-specific details."""
        base = super().get_info()
        return f"{base}, {self.trunk_diameter}cm diameter"

    def produce_shade(self) -> str:
        """
        Return a message describing shade produced by the tree.

        Uses a simple estimate based on trunk diameter to generate a
        readable number.
        """
        shade_area = self.trunk_diameter * 1.56
        return (f"{self.name} provides {shade_area:.0f} square meters "
                f"of shade\n")


class Vegetable(Plant):
    """A plant type that has a harvest season and nutritional value."""

    def __init__(self, name, height, age_days, harvest_season,
                 nutritional_value) -> None:
        """Initialize a vegetable with common plant data plus extra data."""
        super().__init__(name, height, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        """Return a summary string including vegetable-specific details."""
        base = super().get_info()
        return f"{base}, {self.harvest_season} harvest"

    def describe_nutrition(self) -> str:
        """Return a message describing the vegetable's nutritional value."""
        return f"{self.name} is rich in {self.nutritional_value}\n"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Lily", 35, 40, "white"),
    ]
    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 300, 1200, 30),
    ]
    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 20, 70, "spring", "beta-carotene"),
    ]

    for flower in flowers:
        print(f"{flower.name} (Flower): {flower.get_info()}")
        print(flower.bloom())

    for tree in trees:
        print(f"{tree.name} (Tree): {tree.get_info()}")
        print(tree.produce_shade())

    for veg in vegetables:
        print(f"{veg.name} (Vegetable): {veg.get_info()}")
        print(veg.describe_nutrition())
