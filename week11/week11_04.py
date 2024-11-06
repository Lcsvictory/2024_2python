# week11_04.py

class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.dept = ""
        self.year = 0


students = []
for i in range(3):
    print("[" + str(i + 1) + "]")
    stu = Student()
    stu.id = input("학번:")
    stu.name = input("이름:")
    stu.dept = input("학과:")
    stu.year = int(input("생년(yyyy):"))
    students.append(stu)

for i in students:
    print(i.name)
