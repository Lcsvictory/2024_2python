# week11_06.py

class Human():
    def __init__(self):
        self.name = "김인하"
        self.age = 20
    def func(self, name, age):
        self.name = name
        #self.age = age
        print(age)

h = Human()
print(h.name)
print(h.age)


h = Human()
h.func("김인하", 20)
print(h.name)
print(h.age)
