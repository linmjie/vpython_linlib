import vpython as vp
from typing import Callable

# standardAttributes is parent class of most vpython objects
_clickableObjectRegistry: dict[
        vp.standardAttributes, Callable[[], None]
] = {}

def registerClickable(obj: vp.standardAttributes, callback: Callable[[], None]):
    _clickableObjectRegistry[obj] = callback

def _clickEvent(ev):
    global _clickableObjectRegistry
    picked = vp.scene.mouse.pick
    if picked == None:
        return
    callback = _clickableObjectRegistry.get(picked)
    if callback != None:
        callback()

# explicitly non in main method
vp.scene.bind('click', _clickEvent)

class Keys:
    up: str = 'up'
    down: str = 'down'
    left: str = 'left'
    right: str = 'right'
    home: str = 'home'
    end: str = 'end'
    page_up: str = 'pageup'
    page_down: str = 'pagedown'
    insert: str = 'insert'
    delete: str = 'delete'
    backspace: str = 'backspace'
    tab: str = 'tab'
    enter: str = '\n'
    shift: str = 'shift'
    ctrl: str = 'ctrl'
    alt: str = 'alt'
    caps_lock: str = 'caps lock'
    escape: str = 'escape'
    f1: str = 'f1'
    f2: str = 'f2'
    f3: str = 'f3'
    f4: str = 'f4'
    f5: str = 'f5'
    f6: str = 'f6'
    f7: str = 'f7'
    f8: str = 'f8'
    f9: str = 'f9'
    f10: str = 'f10'
    f11: str = 'f11'
    f12: str = 'f12'
