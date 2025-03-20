class MinutesConverter:
    def __init__(self, minutes):
        self.min=minutes
    def	toHours(self):
        return self.min//60
    def toSeconds(self):
        return self.min*60
    def toDays(self):
        return self.min//1440
num1=MinutesConverter(15620)
num2=MinutesConverter(7500)
num3=MinutesConverter(25600)
print(num1.toHours())
print(num2.toSeconds())
print(num3.toDays())