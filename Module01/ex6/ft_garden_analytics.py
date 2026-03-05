"""
This module builds a small garden management and analytics system.

It demonstrates:
- A GardenManager that handles multiple gardens
- A nested GardenStats helper for calculating statistics
- An inheritance chain: Plant -> FloweringPlant -> PrizeFlower
- Instance methods vs class methods vs static methods
"""


class Plant:
    """Base plant with a name and height (cm)."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a plant with a name and a non-negative height."""
        self.name = name
        self.height = height

    def grow(self) -> None:
        """Increase the plant height by 1 cm."""
        self.height += 1

    def info(self) -> str:
        """Return a short string describing this plant."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """A plant that can bloom and has a flower color."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a flowering plant with a color and bloom state."""
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        """Set this plant as blooming."""
        self.is_blooming = True

    def info(self) -> str:
        """Return a string describing this flowering plant."""
        base = super().info()
        state = "blooming" if self.is_blooming else "not blooming"
        return f"{base}, {self.color} flowers ({state})"


class PrizeFlower(FloweringPlant):
    """A flowering plant that can earn prize points."""

    def __init__(
        self, name: str, height: int, color: str, prize_points: int
    ) -> None:
        """Initialize a prize flower with prize points."""
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def info(self) -> str:
        """Return a string describing this prize flower."""
        base = super().info()
        return f"{base}, Prize points: {self.prize_points}"


class GardenManager:
    """Manage multiple gardens and provide analytics."""

    class GardenStats:
        """Helper for computing statistics about a single garden."""

        def __init__(self, initial_heights: dict[str, int]) -> None:
            """Store initial heights to compute total growth later."""
            self._initial_heights = initial_heights

        def total_growth(self, plants: list[Plant]) -> int:
            """Return total growth compared to initial heights."""
            growth = 0
            for p in plants:
                before = self._initial_heights.get(p.name, p.height)
                growth += (p.height - before)
            return growth

        def type_counts(self, plants: list[Plant]) -> tuple[int, int, int]:
            """
            Return counts of (regular, flowering, prize) plants.

            A PrizeFlower is also a FloweringPlant but counted separately here.
            """
            regular = 0
            flowering = 0
            prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    gardens_managed = 0

    def __init__(self) -> None:
        """Initialize an empty manager."""
        self._gardens: dict[str, list[Plant]] = {}
        self._stats: dict[str, GardenManager.GardenStats] = {}

    def add_garden(self, owner: str) -> None:
        """Create an empty garden for an owner if it doesn't exist."""
        if owner not in self._gardens:
            self._gardens[owner] = []
            self._stats[owner] = GardenManager.GardenStats(initial_heights={})
            GardenManager.gardens_managed += 1

    def add_plant(self, owner: str, plant: Plant) -> None:
        """Add a plant to an owner's garden and record its initial height."""
        self.add_garden(owner)
        self._gardens[owner].append(plant)
        self._stats[owner]._initial_heights[plant.name] = plant.height
        print(f"Added {plant.name} to {owner}'s garden")

    def help_all_plants_grow(self, owner: str) -> None:
        """Grow all plants by 1cm and bloom flowering plants."""
        plants = self._gardens.get(owner, [])
        print(f"{owner} is helping all plants grow...")
        for p in plants:
            p.grow()
            if isinstance(p, FloweringPlant):
                p.bloom()
            print(f"{p.name} grew 1cm")

    def garden_report(self, owner: str) -> None:
        """Print a report about an owner's garden and computed analytics."""
        plants = self._gardens.get(owner, [])
        stats = self._stats.get(owner)
        if stats is None:
            print(f"No garden found for {owner}")
            return

        print(f"=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in plants:
            print(f"- {p.info()}")

        total_growth = stats.total_growth(plants)
        regular, flowering, prize = stats.type_counts(plants)
        print(f"\nPlants added: {len(plants)}, Total growth: {total_growth}cm")
        print(
            f"Plant types: {regular} regular, {flowering} flowering, "
            f"{prize} prize flowers\n"
        )

    @staticmethod
    def validate_height(height: int) -> bool:
        """Utility validation: plant heights should be non-negative."""
        return height >= 0

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """
        Create a demo network of gardens.

        This is a class-level constructor (works on the class, not an instance)
        """
        manager = cls()
        manager.add_garden("Alice")
        manager.add_garden("Bob")
        return manager

    @classmethod
    def garden_scores(cls, manager: "GardenManager") -> dict[str, int]:
        """
        Compute simple garden 'scores' for each owner.

        Score is total height of all plants (demo metric).
        """
        scores: dict[str, int] = {}
        for owner, plants in manager._gardens.items():
            scores[owner] = sum(p.height for p in plants)
        return scores


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    gm = GardenManager.create_garden_network()

    gm.add_plant("Alice", Plant("Oak Tree", 100))
    gm.add_plant("Alice", FloweringPlant("Rose", 25, "red"))
    gm.add_plant("Alice", PrizeFlower("Sunflower", 50, "yellow", 10))
    print()

    gm.help_all_plants_grow("Alice")
    print()
    gm.garden_report("Alice")
    print(f"Height validation test: {GardenManager.validate_height(10)}")
    scores = GardenManager.garden_scores(gm)
    print(
        f"Garden scores - Alice: {scores.get('Alice', 0)}, "
        f"Bob: {scores.get('Bob', 0)}"
    )
    print(f"Total gardens managed: {GardenManager.gardens_managed}")
