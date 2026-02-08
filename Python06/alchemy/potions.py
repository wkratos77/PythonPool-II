from alchemy.elements import create_fire, create_water
from alchemy.elements import create_earth, create_air


def healing_potion():
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion():
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion():
    return (
        f"Invisibility potion brewed with {create_air()} and {create_water()}"
    )


def wisdom_potion():
    fire = create_fire()
    water = create_water()
    earth = create_earth()
    air = create_air()
    return (
        "Wisdom potion brewed with all elements: "
        f"{fire}, {water}, {earth}, and {air}"
    )
