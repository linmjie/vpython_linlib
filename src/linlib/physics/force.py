from dataclasses import dataclass, field
from vpython import vector
import vpython as vp

G: float = 6.6743 * (10**-11)

@dataclass
class MassObject():
    obj: vp.standardAttributes
    mass: float
    accel: vector
    vel: vector
    _pos: vector = field(init=False)

    @property
    def pos(self) -> vector:
        self._pos = self.obj.pos
        return self._pos

    @pos.setter
    def pos(self, value):
        if not isinstance(value, vector):
            raise ValueError("Set pos to a vector")
        self.obj.pos = value
        self._pos = value

    @property
    def force(self) -> vector:
        return self.accel * self.mass


_gravMassObjectRegistry: set[MassObject] = set()

def _gravityCycle(rate: int):
    for obj in _gravMassObjectRegistry:
        for secondObj in _gravMassObjectRegistry:
            if obj != secondObj:
                accelMag = getGravitationalAcceleration(secondObj.mass, obj.mass, obj.pos - secondObj.pos)
                accel = accelMag * centerVector(obj.pos, secondObj.pos)
                obj.accel += accel
                obj.vel += obj.accel / rate
                obj.pos += obj.vel / rate

def registerMassObject(obj: vp.standardAttributes, mass: float):
    zero = vector(0, 0, 0)
    massObj = MassObject(obj, mass, zero, zero)
    _gravMassObjectRegistry.add(massObj)

def centerVector(pos: vector, center: vector) -> vector:
    return (pos - center).norm()

def getGravitationalAcceleration(M: float, mass2: float, radius: float):
    return G * M * mass2 / radius**2

def getDragForce(density: float, velocity: float, dragCoefficient: float, crossSectionalArea: float):
    assert dragCoefficient >= -0.05 and dragCoefficient <= 1.05 # a little leway
    return 0.5 * density * velocity**2 * dragCoefficient * crossSectionalArea
