# week12_01.py

class Subject:
    def __init__(self, number, name, teacher=None, grade=None):
        self.number = number
        self.name = name
        self.teacher = teacher
        self.set_grade(grade)

    def set_grade(self, grade):
        if grade != None and (grade < 0 or grade > 4.5):
            self.grade = None
        else:
            self.grade = grade

    def __str__(self):
        return f"[{self.number}] {self.name}"
    def __repr__(self):
        return f"[{self.number}] {self.name}"

sub = Subject("CS0001", "컴퓨터개론", grade=4.9)
sub.set_grade(4.9)
print(sub.grade)

sub = Subject("CS0001", "컴퓨터개론", grade=4.9)
print(sub.grade)

sub = Subject("CS0001", "컴퓨터개론")
print(sub)
print(sub.grade)

class Student:
    def total_score(self):
        if self.subjects:
            scores = [sub.grade for sub in self.subjects if sub.grade != None]
            if scores:
                return sum(scores) /len(scores)
            else:
                return None
        return None
            
    def __init__(self, number, name, dept, birtyear, *subjects):
        self.number = number
        self.name = name
        self.dept = dept
        self.birtyear = birtyear
        if subjects:
            self.subjects = list(subjects)
        else:
            self.subjects = []

        
    def __str__(self):
        return f"[{self.number}] {self.name}"
subs = [
    Subject("CS0001", "자바스크립트", grade=3.6),
    Subject("CS0002", "자바", grade=2.5),
    Subject("CS0003", "C++", grade=4),
    Subject("CS0004", "Golang"),
        ]
stu1 = Student("1", "김인하", "컴퓨터전공", 2024, subs)
print(Subject("CS0001", "자바스크립트", grade=3.6))
print(subs) # __str__()매직메소드가 적용이 왜 안되는가?





















