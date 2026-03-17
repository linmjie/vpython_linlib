from dataclasses import dataclass, fields

class Temperature:
    kelvin: float

    def __init__(self, **tempArg):
        if len(tempArg) != 1:
            raise ValueError('Provide exactly one temperature argument: kelvin, celsius, or fahrenheit')
        name, value = next(iter(tempArg.items()))
        match name:
            case 'kelvin' | 'k' | 'K':
                self.kelvin = value
            case 'celsius' | 'c' | 'C':
                self.kelvin = value + 273.15
            case 'fahrenheit' | 'f' | 'F':
                self.kelvin = (value - 32) * 5/9 + 273.15
            case _:
                raise ValueError(f'Unknown temperature unit "{name}". Use kelvin, celsius, or fahrenheit')

    @property
    def celsius(self) -> float:
        return self.kelvin - 273.15

    @property
    def fahrenheit(self) -> float:
        return (self.kelvin - 273.15) * 9/5 + 32

@dataclass(frozen=True)
class AtmosphereLevel:
    kelvin: float
    altitude: float
    # add more

    def __post_init__(self):
        if self.kelvin < 0:
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
    EXOSPHERE: AtmosphereLevel = AtmosphereLevel(kelvin=2270, altitude=700)
    THERMOSPHERE: AtmosphereLevel = AtmosphereLevel(kelvin=195, altitude=80)
    MESOSPHERE: AtmosphereLevel = AtmosphereLevel(kelvin=270, altitude=50)
    STRATOSPHERE: AtmosphereLevel = AtmosphereLevel(kelvin=210, altitude=15)
    TROPOSPHERE: AtmosphereLevel = AtmosphereLevel(kelvin=300, altitude=0)

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
