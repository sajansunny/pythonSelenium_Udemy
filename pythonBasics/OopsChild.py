from Oops import Calculator


class ChildImplementation(Calculator):

    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 3)

    def getCompleteData(self):
        return self.num + self.summation() + self.num2


obj = ChildImplementation()
print(obj.getCompleteData())
