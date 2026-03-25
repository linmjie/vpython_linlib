from dataclasses import dataclass
from typing import Final
from vpython import vector
import vpython as vp
from ..axis import Axis

from linlib.axis import Axis

G: float = 6.6743 * (10**-11) # m^3/kgs^2
EPSILON_NAUGHT: float = 8.854 * (10**-12) # C^2/Nm^2
K: float = 8.98755 * (10**9) # Nm^2/C^2

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
    dt: float = 1 / rate
    for obj in _gravMassObjectRegistry:
        obj.accel = Axis.ZERO
        for secondObj in _gravMassObjectRegistry:
            if obj != secondObj:
                accelMag: float = getGravitationalAcceleration(secondObj.mass, (obj.pos - secondObj.pos).mag)
                direction: vector = centerVector(obj.pos, secondObj.pos)
                accel: vector = accelMag * direction
                obj.accel += accel
                obj.vel += obj.accel * dt
                obj.pos += obj.vel * dt

def registerMassObject(obj: vp.standardAttributes, mass: float) -> MassObject:
    zero = vector(0, 0, 0)
    massObj = MassObject(obj, mass, zero, zero)
    _gravMassObjectRegistry.add(massObj)
    return massObj

def centerVector(pos: vector, center: vector) -> vector:
    return (center - pos).norm()

def getGravitationalAcceleration(mass: float, radius: float):
    if radius != 0:
        return G * mass / radius**2
    return 0

def getDragForce(density: float, velocity: float, dragCoefficient: float, crossSectionalArea: float):
    assert dragCoefficient >= -0.05 and dragCoefficient <= 1.05 # a little leway
    return 0.5 * density * velocity**2 * dragCoefficient * crossSectionalArea
