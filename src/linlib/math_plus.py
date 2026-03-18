from math import log, e, sin, cos, tan
from vpython import vector

def ln(num: float) -> float:
    return log(e, num)

def csc(num: float) -> float:
    return 1 / sin(num)

def sec(num: float) -> float:
    return 1 / cos(num)

def cot(num: float) -> float:
    return 1 / tan(num)

def approx(num1: float | vector, num2: float | vector, error: float) -> bool:
    if isinstance(num1, float) and isinstance(num2, float):
        return (num1 - error <= num2) and (num1 + error >= num2)
    elif isinstance(num1, vector) and isinstance(num2, vector):
        return approx(num1.x, num2.x, error) \
        and approx(num1.y, num2.y, error) \
        and approx(num1.z, num2.z, error)
    raise NotImplementedError
