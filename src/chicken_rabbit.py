def chicken_rabbit(heads: int, feet: int):
    if not all(isinstance(v, int) and not isinstance(v, bool) for v in (heads, feet)):
        raise TypeError("heads and feet must be integers")

    if heads < 0 or feet < 0:
        return None

    if feet % 2 != 0:
        return None

    min_feet = 2 * heads
    max_feet = 4 * heads

    if feet < min_feet or feet > max_feet:
        return None

    chickens = (4 * heads - feet) // 2
    rabbits = (feet - 2 * heads) // 2

    return (chickens, rabbits)
