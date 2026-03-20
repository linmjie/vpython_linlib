from dataclasses import dataclass, fields
from vpython import vector

G: float = 6.6743 * (10**-11)

def centerVector(pos: vector, center: vector) -> vector:
    return (pos - center).norm()

def getGravitationalAcceleration(mass: float, radius: float):
    return G * mass / radius**2

def getDragForce(density: float, velocity: float, dragCoefficient: float, crossSectionalArea: float):
    assert dragCoefficient >= -0.05 and dragCoefficient <= 1.05 # a little leway
    return 0.5 * density * velocity**2 * dragCoefficient * crossSectionalArea

class Temperature:
    kelvin: float

    def __init__(self, **tempArg):
        if len(tempArg) != 1:
            raise ValueError('Provide exactly one temperature argument: kelvin, celsius, or fahrenheit')
        name, value = next(iter(tempArg.items()))
        match name.capitalize():
            case 'Kelvin' | 'K':
                self.kelvin = value
            case 'Celsius' | 'C':
                self.kelvin = value + 273.15
            case 'Fahrenheit' | 'F':
                self.kelvin = (value - 32) * 5/9 + 273.15
            case _:
                raise ValueError(f'Unknown temperature unit "{name}". Use kelvin, celsius, or fahrenheit')

    @property
    def celsius(self) -> float:
        return self.kelvin - 273.15

    @property
    def fahrenheit(self) -> float:
        return (self.kelvin - 273.15) * 9/5 + 32

    def __str__(self):
        return f'Temperature in kelvin: {self.kelvin}, celcius: {self.celsius}, fahrenheit: {self.fahrenheit}'

    def __add__(self, other):
        if isinstance(other, Temperature):
            return Temperature(kelvin=self.kelvin + other.kelvin)
        if isinstance(other, (float, int)):
            return Temperature(kelvin=self.kelvin + other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Temperature):
            return Temperature(kelvin=self.kelvin - other.kelvin)
        if isinstance(other, (float, int)):
            return Temperature(kelvin=self.kelvin - other)
        return NotImplemented

@dataclass(frozen=True)
class AtmosphereLevel:
    temperature: Temperature 
    density: float # kg/m^3
    altitude: float

    def __post_init__(self):
        if self.temperature.kelvin < 0:
            raise ValueError('Temperature in kelvin cannot be negative')

class _MetaAtmosphereLevelsIter(type):
    def __iter__(cls):
        attrs = (
            getattr(cls, attr)
            for attr in dir(cls)
            if not attr.startswith('__')
            and isinstance(getattr(cls, attr), AtmosphereLevel)
        )
        # Guarentee order based on ascending altitude
        return iter(sorted(attrs, key=lambda lvl: lvl.altitude))

# All values for atmosphere levels are measured from the bottom
class AtmosphereLevels(metaclass=_MetaAtmosphereLevelsIter):
    EXOSPHERE: AtmosphereLevel = AtmosphereLevel(Temperature(k=2270), density=10**-10, altitude=700)
    THERMOSPHERE: AtmosphereLevel = AtmosphereLevel(Temperature(k=195), density=0.000008, altitude=80)
    MESOSPHERE: AtmosphereLevel = AtmosphereLevel(Temperature(k=270), density=0.001, altitude=50)
    STRATOSPHERE: AtmosphereLevel = AtmosphereLevel(Temperature(k=210), density=0.364, altitude=15)
    TROPOSPHERE: AtmosphereLevel = AtmosphereLevel(Temperature(k=300), density=1.225, altitude=0)

    @staticmethod
    def getGradiant(altitude: float) -> AtmosphereLevel:
        previousLevel: AtmosphereLevel = AtmosphereLevels.TROPOSPHERE
        for level in AtmosphereLevels:
            if altitude > previousLevel.altitude:
                previousLevel = level
            else:
                gradient = {}
                altDiff: float = level.altitude - previousLevel.altitude
                assert altDiff >= 0
                altDiffRatio: float = (altitude - level.altitude) / altDiff
                for field in fields(AtmosphereLevel):
                    lower = getattr(previousLevel, field.name)
                    higher = getattr(level, field.name)
                    gradient[field.name] = lower + altDiffRatio * (higher - lower)
                gradient['altitude'] = altitude
                return AtmosphereLevel(**gradient)
        else:
            return AtmosphereLevels.EXOSPHERE
