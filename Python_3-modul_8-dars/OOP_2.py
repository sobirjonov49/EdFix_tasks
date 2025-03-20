class Calculator:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        return self.num1+self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2
    def sub(self):
        return self.num1-self.num2
N1=Calculator(25,12)
N2=Calculator(9,2)
N3=Calculator(65,13)
N4=Calculator(15,20)
print(N1.mul())
print(N2.sum())
print(N3.div())
print(N4.sub())