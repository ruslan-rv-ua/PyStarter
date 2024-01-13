class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    @property
    def area(self):
        return self.width * self.height

r = Rectangle(7, 9)
a = r.area

class TemperatureConverter:
    def __init__(self, celsius=0):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError('Temperature below -273.15°C is not possible')
        self._celsius = value

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    @property
    def kelvin(self):
        return self.celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        self.celsius = value - 273.15

    def __repr__(self) -> str:
        return f'TemperatureConverter({self.celsius})'
    
    def __str__(self) -> str:
        return f'{self.celsius}°C'
    
t = TemperatureConverter()
k=t.kelvin
f=t.fahrenheit
# t = TemperatureConverter(-1000)