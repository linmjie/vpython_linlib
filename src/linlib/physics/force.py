from dataclasses import dataclass
from typing import Final, Self
from vpython import vector
import vpython as vp

G: float = 6.6743 * (10**-11)

@dataclass
class MassObject():
    obj: Final[vp.standardAttributes]
    mass: float
    accel: vector
    vel: vector

    @property
    def pos(self) -> vector:
        return self.obj.pos

    @pos.setter
    def pos(self, value):
        if not isinstance(value, vector):
            raise ValueError("Set pos to a vector")
        self.obj.pos = value

    @property
    def force(self) -> vector:
        return self.accel * self.mass

    def __str__(self):
        return f'Object: {self.obj}, mass: {self.mass}kg, ' \
               f'(vectors) acceleration: {self.accel}, velocity: {self.vel}, position: {self.pos}'

    def __hash__(self):
        return id(self.obj)

_gravMassObjectRegistry: set[MassObject] = set()

def _gravityCycle(rate: int):
    for obj in _gravMassObjectRegistry:
        for secondObj in _gravMassObjectRegistry:
            if obj != secondObj:
                accelMag = getGravitationalAcceleration(secondObj.mass, obj.mass, (obj.pos - secondObj.pos).mag)
                accel = accelMag * centerVector(obj.pos, secondObj.pos)
                obj.accel += accel
                obj.vel += obj.accel / rate
                obj.pos += obj.vel / rate

def registerMassObject(obj: vp.standardAttributes, mass: float) -> MassObject:
    zero = vector(0, 0, 0)
    massObj = MassObject(obj, mass, zero, zero)
    _gravMassObjectRegistry.add(massObj)
    return massObj

def centerVector(pos: vector, center: vector) -> vector:
    return (pos - center).norm()

def getGravitationalAcceleration(M: float, mass2: float, radius: float):
    if radius != 0:
        return G * M * mass2 / radius**2
    return 0

def getDragForce(density: float, velocity: float, dragCoefficient: float, crossSectionalArea: float):
    assert dragCoefficient >= -0.05 and dragCoefficient <= 1.05 # a little leway
    return 0.5 * density * velocity**2 * dragCoefficient * crossSectionalArea
