class Solution:
    def convertTemperature(self, Celsius: float) -> list [float]:
       Kelvin = Celsius + 273.15
       Fahrenheit = Celsius * 1.80 + 32.00 
       ans = [Kelvin, Fahrenheit]
       return ans