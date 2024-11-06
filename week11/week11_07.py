# week11_07.py

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
    def __str__(self): # return값은 반드시 str
        return f"x = {self.x}, y = {self.y}"
    
p1 = Point()
print(p1.x, p1.y)
print(p1)
print(1)
#print(int(1).__str__)
#print(int(1).__str__())
print(1.1)

p2 = Point(10.1, 20.2)
print(p2.x, p2.y)

class Rect:
    def __init__(self, x=0.0, y=0.0, w=0.0, h=0.0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
r1 = Rect()
print(r1.x, r1.y, r1.w, r1.h)


class Subject:
    def __init__(self, idd, name, lect=None, score=None):
        self.idd = idd
        self.name = name
        self.lecturer = lect
        self.score = score














class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.dept = ""
        self.year = 0.0
        #매개변수 4개 필요

class Rect2:
    def __init__(self, sp=Point(), w=0.0, h=0.0):
        self.sp = sp
        self.w = w
        self.h = h
        
r = Rect2()
r = Rect2(Point(2,3), 10, 20)

class Rect3:
    def __init__(self, sp=Point(), ep=Point()):
        self.sp = sp
        self.ep = ep
        
r = Rect3()
r = Rect3(Point(1,3), Point(2,6))
print(r.sp.x, r.sp.y)
print(r.ep.x, r.ep.y)

class Temp(Point):
    def __init__(self):
        super().__init__()
t1 = Temp()
print(t1.x, t1.y)



        
