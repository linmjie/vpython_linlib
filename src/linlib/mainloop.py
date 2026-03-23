from typing import Callable, overload
import vpython as vp
import inspect 
from sys import argv

from linlib.physics import force

# Mostly here to please pyright on type annotations
@overload
def activateMain(callback: Callable[[list[str]], None], rate: int) -> None: ...
@overload
def activateMain(callback: Callable[[], None], rate: int) -> None: ...

def activateMain(callback, rate: int) -> None:
    sig = inspect.signature(callback)
    params = list(sig.parameters.values())
    if params: # assume Callable[[list[str]], None] (only validates that param list len > 0)
        while True:
            vp.rate(rate)
            force._gravityCycle(rate)
            callback(argv)
    else: # assume Callable[[None], None] (only validates there are no parameters)
        while True:
            vp.rate(rate)
            force._gravityCycle(rate)
            callback()
