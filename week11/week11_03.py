# week11_03.py

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
        
p1 = Point()
print(p1.x, p1.y)


class Rect:
    def __init__(self, x=0.0, y=0.0, w=0.0, h=0.0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
r1 = Rect()
print(r1.x, r1.y, r1.w, r1.h)


class Subject:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.lecturer = ""
        self.score = 0.0

class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.dept = ""
        self.year = 0.0

class Rect2:
    def __init__(self, sp=Point(), w=0.0, h=0.0):
        self.sp = sp
        self.w = w
        self.h = h

class Rect3:
    def __init__(self, sp=Point(), ep=Point()):
        self.sp = sp
        self.ep = ep

r = Rect3(Point(1,3), Point(2,6))
print(r.sp.x, r.sp.y)
print(r.ep.x, r.ep.y)

class Temp(Point):
    def __init__(self):
        super().__init__(self)
t1 = Temp()
print(t1.x, t1.y)



        
