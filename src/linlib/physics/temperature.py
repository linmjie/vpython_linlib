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
