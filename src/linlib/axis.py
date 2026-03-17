from vpython import vec, vector

class Axis:
    ZERO: vector = vec(0, 0, 0)
    X: vector = vec(1, 0, 0)
    Y: vector = vec(0, 1, 0)
    Z: vector = vec(0, 0, 1)
    NEG_X: vector = vec(-1, 0, 0)
    NEG_Y: vector = vec(0, -1, 0)
    NEG_Z: vector = vec(0, 0, -1)
