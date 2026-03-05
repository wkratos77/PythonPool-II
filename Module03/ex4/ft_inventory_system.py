import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    if len(sys.argv) == 1:
        print(
            "No inventory data provided. "
            "Usage: python3 ft_inventory_system.py item:quantity ..."
        )
        sys.exit(1)
    inventory = {}
    for arg in sys.argv[1:]:
        parts = arg.split(":")
        if len(parts) != 2 or parts[0] == "" or parts[1] == "":
            print(
                f"Invalid format: {arg}. "
                "Expected item:quantity (e.g., sword:1)."
            )
            sys.exit(1)

        name = parts[0]
        try:
            quantity = int(parts[1])
        except ValueError:
            print(
                f"Invalid quantity for {name}: {parts[1]}. "
                "Quantity must be a number."
            )
            sys.exit(1)
        current = inventory.get(name, 0)
        inventory[name] = current + quantity

    total = sum(inventory.values())
    print("Total items in inventory:", total)
    print("Unique item types:", len(inventory))
    print()

    print("=== Current Inventory ===")
    for name, quantity in inventory.items():
        percentage = (quantity / total * 100)
        if quantity > 1:
            print(f"{name}: {quantity} units ({percentage:.1f}%)")
        else:
            print(f"{name}: {quantity} unit ({percentage:.1f}%)")
    print()

    print("=== Inventory Statistics ===")
    maxq = max(inventory.values())
    minq = min(inventory.values())
    max_item = [
        name for name, quantity in inventory.items()
        if quantity == maxq
    ][0]

    min_item = [
        name for name, quantity in inventory.items()
        if quantity == minq
    ][0]
    if maxq > 1:
        print(f"Most abundant: {max_item} ({maxq} units)")
    else:
        print(f"Most abundant: {max_item} ({maxq} unit)")
    if minq > 1:
        print(f"Least abundant: {min_item} ({minq} units)")
    else:
        print(f"Least abundant: {min_item} ({minq} unit)")
    print()

    print("=== Item Categories ===")
    categories = {"Moderate": {}, "Scarce": {}}
    for name, quantity in inventory.items():
        if quantity >= 5:
            categories["Moderate"][name] = quantity
        else:
            categories["Scarce"][name] = quantity
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")
    print()

    print("=== Management Suggestions ===")
    restock = []
    for name, quantity in categories["Scarce"].items():
        if quantity == 1:
            restock.append(name)
    print("Restock needed:", restock)
    print()

    demo = {}
    demo.update(inventory)

    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", list(inventory.keys()))
    print("Dictionary values:", list(inventory.values()))
    print("Sample lookup - 'sword' in inventory:", "sword" in inventory)
