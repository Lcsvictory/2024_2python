# week11_02.py

class Human:
    def __init__(self): # 파라미터
        self.name = "김인하"
        self.age = 20
    def __str__(self):
        return "Human클래스의 기본 출력 문장입니다."

h = Human()
print(h.name)

h2 = Human()
print(h2.name)

#h3 = h2

h.name = "박인하"
h2.name = "최인하"

print(id(h), id(h2))
print(type(h) == type(h2))
print(h.name == h2.name)
print(h.age == h2.age)
