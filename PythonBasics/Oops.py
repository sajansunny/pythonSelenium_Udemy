# self keyword is mandatory while calling variables inside the methods


class Calculator:

    num = 100       # class variable

    def __init__(self, a, b):       # constructor
        self.firstNumber = a        # instance variable
        self.secondNumber = b
        print("I am called automatically while creating the object of the class")

    def getdata(self):
        print("I am now executing method inside the class")

    def summation(self):
        return self.firstNumber + self.secondNumber + self.num


obj = Calculator(2, 3)
obj.getdata()
print(obj.num)
print(obj.summation())

obj = Calculator(4, 5)
obj.getdata()
print(obj.num)
print(obj.summation())
