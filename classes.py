class FirstClass:
    pass


egclass = FirstClass()
print(type(egclass))


class SecondClass:
    def __int__(self, name, symbol):
        self.name = name
        self.symbol = symbol


eg1 = SecondClass()
eg2 = SecondClass()
eg1.name = 'one'
eg1.symbol = 1
eg2.name = 'two'
eg2.symbol = 2
print(eg1.name, eg1.symbol)
print(eg2.name, eg2.symbol)

print(dir(SecondClass))


class MultipleClass:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def square(self):
        return self.symbol * self.symbol

    def cube(self):
        return self.symbol * self.symbol * self.symbol

    def multiply(self, x):
        return self.symbol * x


eg4 = MultipleClass('Five', 5)
print(eg4.square())
print(eg4.cube())
print(eg4.multiply(20))





