from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    lead = lead_to_gold()
    heal = healing_potion()
    return f"Philosopher's stone created using {lead} and {heal}"


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
