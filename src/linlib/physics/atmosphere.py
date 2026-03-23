from dataclasses import dataclass, fields
from temperature import Temperature

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
