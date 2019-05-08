from abc import ABC, abstractmethod
from numbers import Real

class Temperature(ABC):

    @abstractmethod
    def __init__(self, temp):
        self.temperature = temp

    def __str__(self):
        return f"{round(self.temperature)}\u00b0{self.__class__.__name__[0]}"

    def __repr__(self):
        return self.__class__.__name__ + f"({self.temperature})"

    def above_freezing(self):
        return True if self.to_celsius().temperature > 0 else False

    @abstractmethod
    def to_celsius(self):
        pass

    @abstractmethod
    def to_fahrenheit(self):
        pass

    @abstractmethod
    def to_kelvin(self):
        pass

    @property
    @abstractmethod
    def temperature(self):
        return self.__temperature

    @temperature.setter
    @abstractmethod
    def temperature(self, temp):
        if isinstance(temp, Real):
            self.__temperature = temp
        else:
            self.__temperature = 0

class Fahrenheit(Temperature):

    def __init__(self, temp):
        super().__init__(temp)

    def to_fahrenheit(self):
        return self

    def to_celsius(self):
        return Celsius((self.temperature - 32) / 1.8)

    def to_kelvin(self):
        return Kelvin(self.to_celsius().temperature + 273.16)

    @property
    def temperature(self):
        return super().temperature

    @temperature.setter
    def temperature(self, temp):
        super(type(self), type(self)).temperature.__set__(self, temp)

class Celsius(Temperature):
    def __init__(self, temp):
        super().__init__(temp)

    def to_celsius(self):
        return self

    def to_fahrenheit(self):
        return Fahrenheit(32 + (1.8 * self.temperature))

    def to_kelvin(self):
        return Kelvin(self.temperature + 273.16)

    @property
    def temperature(self):
        return super().temperature

    @temperature.setter
    def temperature(self, temp):
        super(type(self), type(self)).temperature.__set__(self, temp)


class Kelvin(Temperature):
    def __init__(self, temp):
        super().__init__(temp)

    def to_celsius(self):
        return Celsius(self.temperature - 273.16)

    def to_fahrenheit(self):
        return Fahrenheit(self.to_celsius().to_fahrenheit().temperature)

    def to_kelvin(self):
        return self

    @property
    def temperature(self):
        return super().temperature

    @temperature.setter
    def temperature(self, temp):
        super(type(self), type(self)).temperature.__set__(self, temp)


list = [Celsius(-20), Celsius(35), Celsius(-132), Celsius(220),
        Fahrenheit(32), Fahrenheit(475), Fahrenheit(-40), Fahrenheit(0),
        Kelvin(273), Kelvin(98), Kelvin(10), Kelvin(0)]
listC = []
listF = []
listK = []

for t in list:
    print(t)
    if(t.above_freezing()):
        print("Powyżej punktu zamarzania")

    listC.append(t.to_celsius())
    listF.append(t.to_fahrenheit())
    listK.append(t.to_kelvin())
print(25*"-")

print("\nLista (w \u00b0C, poniżej punktu zamarzania)")
for tC in listC:
    if not tC.above_freezing():
        print(tC)

print("\nLista (w \u00b0F, poniżej punktu zamarzania)")
for tF in listF:
    if not tF.above_freezing():
        print(tF)

print("\nLista (w \u00b0K, poniżej punktu zamarzania)")
for tK in listK:
    if not tK.above_freezing():
        print(tK)