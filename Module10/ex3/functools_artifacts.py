import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return functools.reduce(operator.add, spells, 0)
    elif operation == "multiply":
        return functools.reduce(operator.mul, spells, 1)
    elif operation == "max":
        return functools.reduce(max, spells)
    elif operation == "min":
        return functools.reduce(min, spells)
    else:
        raise ValueError(
            "Invalid operation. Use 'add', 'multiply', 'max', or 'min'.")


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire = functools.partial(base_enchantment, 50, "fire")
    ice = functools.partial(base_enchantment, 50, "ice")
    lightning = functools.partial(base_enchantment, 50, "lightning")
    return {
        'fire_enchant': fire,
        'ice_enchant': ice,
        'lightning_enchant': lightning
    }


def memoized_fibonacci(n: int) -> int:
    @functools.lru_cache(maxsize=None)
    def fib(n) -> int:
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)
    return fib(n)


def spell_dispatcher() -> callable:

    @functools.singledispatch
    def dispatch(arg) -> str:
        return "Unknown spell"

    @dispatch.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg}"

    @dispatch.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @dispatch.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {', '.join(map(str, arg))}"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [30, 30, 40]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))

    print("\nTesting memoized Fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
