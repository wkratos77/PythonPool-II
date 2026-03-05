"""Garden Security System: Validate plant data before updates."""


class SecurePlant:
    """Manage plant data with validation on height and age."""

    def __init__(self, name, height, age_days) -> None:
        """Initialize a secure plant and set validated attributes."""
        self.name = name
        self._height = 0
        self._age_days = 0

        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age_days)

    def set_height(self, new_height) -> None:
        """Set the plant height if the value is non-negative."""
        if new_height < 0:
            print(
                f"\nInvalid operation attempted: height {new_height}cm "
                "[REJECTED]"
            )
            print("Security: Negative height rejected\n")
            return
        self._height = new_height
        print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, new_age) -> None:
        """Set the plant age if the value is non-negative."""
        if new_age < 0:
            print(
                f"\nInvalid operation attempted: age {new_age} days "
                "[REJECTED]"
            )
            print("Security: Negative age rejected\n")
            return
        self._age_days = new_age
        print(f"Age updated: {self._age_days} days [OK]")

    def get_height(self) -> int:
        """Return the plant height."""
        return self._height

    def get_age(self) -> int:
        """Return the plant age in days."""
        return self._age_days

    def display_info(self) -> None:
        """Print the plant's current status."""
        print(
            f"Current plant: {self.name} ({self._height}cm, "
            f"{self._age_days} days)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    plant.display_info()
