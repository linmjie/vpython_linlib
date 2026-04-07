import random

def randomList(quantity: int, min: int | float = 0, max: int | float = 10) \
-> list[int] | list[float]:
    useFloatType: bool = isinstance(min, float) or isinstance(max, float)
    ls = []
    for _ in range(quantity):
        ls.append(random.uniform(min, max) if useFloatType \
                  else random.randint(min, max)) #pyright: ignore
    return ls
