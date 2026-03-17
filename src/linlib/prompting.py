from typing import Callable

def prompt(promptStr: str, fn: Callable[[str], str]) -> bool:
    save = fn(f'{promptStr} (y/n) ')
    while save != 'y' or save != 'n':
        save = fn(f'{promptStr} (y/n)')
    return save == 'y'
