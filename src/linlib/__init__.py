from .math_plus import ln, csc, sec, cot # no star import to avoid name conflicts
from .physics.atmosphere import *
from .physics import force
from .physics.temperature import Temperature
from .prompting import *

from vpython import * #pyright: ignore
from .memory import *
from .axis import *
from .key_input import *
from .mainloop import activateMain

# clean up namespace
del math_plus
del physics
del prompting
# del vpython
del axis
del key_input
del memory
del vp
