

myFile = "C:/A202001098/leechungseong_02.txt"

scores = {}

f = open(myFile,"a")

while True:
    scores['k'] = int(input("kor:"))
    scores['m'] = int(input("mat:"))
    scores['e'] = int(input("eng:"))

    data = ""
    for i in scores.keys():
        if data:
            data += "|"
        data += (f"{i},{scores[i]}")
    f.write(f"{data}\n")
    if input("종료:(Y)").strip().upper() == "Y":
        break
f.close()












'''
myFile = "C:/A202001098/leechungseong_01.txt"

scores = {}

f = open(myFile,"a")

while True:
    scores['k'] = int(input("kor:"))
    scores['m'] = int(input("mat:"))
    scores['e'] = int(input("eng:"))

    for i in scores.keys():
        f.write(f"{i},{scores[i]}\n")
    if input("종료:(Y)").strip().upper() == "Y":
        break
f.close()
'''
