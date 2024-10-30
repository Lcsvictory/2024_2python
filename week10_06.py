# week10_06.py

class Score:
    def __init__(self, kor=0, eng=0, mat=0):
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def avg(self):
        return (self.kor + self.eng + self.mat) / 3
scores3 = Score()
print(scores3.kor)
scores3.kor = 100
print(scores3.kor)

scores4 = Score(10, mat=20, eng=90)


print(scores3.kor, scores3.avg())
'''

scores1 = {10, 20, 30}
scores2 = {'k':10, 'm':20, 'e':30}

def avg_list(datas) :
    return sum(datas) / len(datas)

def avg_dict(datas) :
    return sum(datas.values()) / len(datas)


print(avg_list(scores1))
print(avg_dict(scores2))
'''
